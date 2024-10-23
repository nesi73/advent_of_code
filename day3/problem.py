from read_txt import contents
import numpy as np

numbers = {}
row, col = len(contents), len(contents[0])
matrix=np.zeros((row,col))

for row, content in enumerate(contents):

    search_number = ''
    same_number = []

    for column, c in enumerate(content):
        try:
            number = int(c)
            search_number+=c
            same_number.append(column)
        except:
            if len(same_number) > 0:
                for col in same_number:
                    matrix[row, col] = int(search_number)
            matrix[row, column] = -1 if c != '.' else -2

            same_number = []
            search_number = ''
print(matrix)
where_symbol = np.where(matrix == -1)
sum_num = 0

for i in range(len(where_symbol[0])):
    row, col = where_symbol[0][i], where_symbol[1][i]

    # TODO: restricciones por si se va fuera de la matriz
    possible_numbers = []   
    possible_numbers.extend(matrix[row-1, col-1:col+2])
    possible_numbers.extend(matrix[row, col-1:col+2])
    possible_numbers.extend(matrix[row + 1, col-1:col+2])

    for num in possible_numbers:
        sum_num += num if num != -2 and num != -1 else 0
    
print(sum_num)