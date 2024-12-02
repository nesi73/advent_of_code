import numpy as np

class Sensor():
    def __init__(self, path):
        self.histories = self.analyze_surrounding(path)

    def analyze_surrounding(self, path):
        print(f"Reading {path} file")

        histories = []
        with open(path, "r") as f:
            lines = f.readlines()

            for line in lines:
                histories.append(line.strip().split(" "))
        
            f.close()
        return np.array(histories).astype(int)
    
    def numbers_between_two_values(self, num1:int, num2:int):
        # comprobate if are the same simbol
        if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
            num = abs(abs(num1) - abs(num2))
        else:
            num = abs(num1) + abs(num2)
        
        return num if num1 < num2 else -num

    def predict_next_values(self, history):
        
        all_information = [history]
        information = list(history)

        while np.any(np.array(history) != 0):

            information = []
            for i in range(len(history) - 1):
                information.append(self.numbers_between_two_values(history[i], history[i+1]))

            all_information.append(information)
            history = information

        return all_information
    
    def extrapolate_history(self, history):
        final_num = 0

        reverse_history = history[::-1]
        for i in range(len(reverse_history) - 1):
            final_num = reverse_history[i + 1][0] - final_num
        
        return final_num
    
sensor = Sensor("input2.txt")

result = 0
for history in sensor.histories:
    information = sensor.predict_next_values(history)
    num = sensor.extrapolate_history(information)
    result += num

print(result)