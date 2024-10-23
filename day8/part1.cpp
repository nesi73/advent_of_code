#include <iostream>
#include <fstream>
#include <sstream>
#include <regex>
#include <map>
#include <vector>
#include <string>

using namespace std;

tuple<vector<string>, map<string, map<string, string>>> read_map(const string& txt_file) 
{
    map<string, map<string, string>> map_dict;

    ifstream f(txt_file);
    if (!f.is_open()) {
        cerr << "Error: Could not open file " << txt_file << endl;
        return {};
    }

    string input_txt((istreambuf_iterator<char>(f)), istreambuf_iterator<char>());
    f.close();

    // Leer instrucciones y aplicar regex
    stringstream ss(input_txt);
    string line, key, left, right;
    vector<string> instructions;

    // Obtener la primera línea (instrucciones)
    while (getline(ss, line)) {
        if (instructions.empty()) 
        {
            for (char& c : line) 
            {
                instructions.push_back(std::string(1, c));
            }
        }
        else if (line != "")
        {
            key = line.substr(0, line.find("="));
            left = line.substr(line.find("(") + 1, 3);
            right = line.substr(line.find(",") + 1, 4);
            // remove spaces
            key.erase(remove(key.begin(), key.end(), ' '), key.end());
            left.erase(remove(left.begin(), left.end(), ' '), left.end());
            right.erase(remove(right.begin(), right.end(), ' '), right.end());

            map_dict[key] = { {"L", left}, {"R", right} };
        }
    }
    return {instructions, map_dict};
}

int recursive_map_search(vector<string> instructions, map<string, map<string, string>> map_dict, string key, int cont)
{
    //std::cout << key << " -> ";
    if (key == "ZZZ")
    {
        return cont;
    } 
    else
    {
        string current_instruction = instructions[0];
        instructions.erase(instructions.begin());
        instructions.push_back(current_instruction);
        
        return recursive_map_search(instructions, map_dict, map_dict[key][current_instruction], cont + 1);
    }
}

int main(int argc, char* argv[])
{
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <file.txt>" << endl;
        return 1;
    }

    const auto current_map = read_map(argv[1]);
    
    vector<string> instructions = get<0>(current_map);
    map<string, map<string, string>> map_dict = get<1>(current_map);
    
    int total_movs = recursive_map_search(instructions, map_dict, map_dict.begin()->first, 0);
    cout << "Total movements: " << total_movs << endl;
    return 0;
}