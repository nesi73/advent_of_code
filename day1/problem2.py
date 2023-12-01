import read_txt
from a import example

numbers_dict={
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def is_number(caracter):
    number = -1

    try:
        number = int(caracter)
    except:
        pass
    return number

def inicialize_graph():

    numbers = ['one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    inverse_numbers = [number[::-1] for number in numbers]
    
    graph = {}
    current_graph = {}

    inverse_graph = {}
    inverse_current_graph = {}

    for number in range(len(numbers)):
        current_graph = graph
        inverse_current_graph = inverse_graph

        for i in range(len(numbers[number])):
            letter = numbers[number][i]
            inverse_letter = inverse_numbers[number][i]

            if letter not in current_graph:
                current_graph.update({letter:{}})
            if inverse_letter not in inverse_current_graph:
                inverse_current_graph.update({inverse_letter:{}})

            current_graph = current_graph[letter]
            inverse_current_graph = inverse_current_graph[inverse_letter]
    
    return graph, inverse_graph
        

def search_numbers(line, graph, inverse_graph):

    i = 0
    j = len(line) - 1
    found_solution = False
    first_number, second_number = -1, -1
    current_graph_i=graph
    current_graph_j=inverse_graph
    number_1_str = ''
    number_2_str = ''

    number_1_str_second = ''
    number_2_str_second = ''

    while i <= len(line) - 1 and j >= 0 and not found_solution:
        
        first_number = is_number(line[i])  if first_number == -1 else first_number
        second_number = is_number(line[j]) if second_number == -1 else second_number

        if first_number == -1:
            if line[i] in current_graph_i:
                current_graph_i = current_graph_i[line[i]]
                number_1_str += line[i]
                if len(current_graph_i) == 0:
                    first_number = numbers_dict[number_1_str]
                    number_1_str = ''
                    current_graph_i = graph
                number_1_str_second=''
            elif number_1_str_second == '':
                number_1_str = ''
                current_graph_i = graph
            else:
                number_1_str = number_1_str_second
                current_graph_i = graph[number_1_str_second]
                if line[i] in current_graph_i:
                    current_graph_i = current_graph_i[line[i]]
                    number_1_str += line[i]
                number_1_str_second = ''

            if line[i] in graph:
                number_1_str_second = line[i]

        if second_number == -1:
            if line[j] in current_graph_j:
                print(line[j])
                current_graph_j = current_graph_j[line[j]]
                number_2_str += line[j]
                if len(current_graph_j) == 0:
                    second_number = numbers_dict[number_2_str[::-1]]
                    number_2_str = ''
                    current_graph_j = inverse_graph
            elif number_2_str_second == '':
                number_2_str = ''
                current_graph_j = inverse_graph
            else:
                number_2_str = number_2_str_second
                current_graph_j = inverse_graph[number_2_str_second]
                if line[j] in current_graph_j:
                    current_graph_j = current_graph_j[line[j]]
                    number_2_str += line[j]
                number_2_str_second = ''

            if line[j] in inverse_graph:
                number_2_str_second = line[j]
            


        found_solution = True if first_number != -1 and second_number != -1 else False
        i += 1
        j -= 1

    if first_number != -1 and second_number == -1:
        second_number = first_number
    elif first_number == -1 and second_number != -1:
        first_number = second_number

    return int(str(first_number) + str(second_number))


graph, inverse_graph=inicialize_graph()
sum = 0
for line in read_txt.contents:

    # print(line, ' : ', search_numbers(line, graph, inverse_graph))
    line='bcxvhcjbhsxbgbrj28fivenhk'
    print(line)
    a_ = search_numbers(line, graph, inverse_graph)
    b = example(line+'\n')
    if a_ != b:
        print(line, a_, b)

print(sum)