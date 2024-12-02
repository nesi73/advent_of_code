import numpy as np

def read_input(path):
    D = open(path).read().strip()
    L = D.split('\n')

    all_matrix = []
    matrix = []
    for l in L:
        if l == '':
            all_matrix.append(matrix)
            matrix = []
        else:
            matrix.append([c for c in l])
    all_matrix.append(matrix)
    return all_matrix

def search_difference(row1, row2):
    pos = -1
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            if pos != -1:
                return -1
            pos = i

    return 1

def search_mirror(matrix, i):
    if i + 1 >= len(matrix):
        return -1
    elif search_difference(matrix[i], matrix[i+1]) != -1:
        cont = is_perfect_reflected(matrix, i, i+1, 0)
        if  cont != -1:
            return i + 1
        else:
            return search_mirror(matrix, i+1)
    else:
        return search_mirror(matrix, i+1)

def is_perfect_reflected(matrix, left, rigth, cont):
    if left < 0 or rigth >= len(matrix):
        return cont
    elif search_difference(matrix[left], matrix[rigth]) != -1:
        return is_perfect_reflected(matrix, left-1, rigth+1, cont+1)
    else:
        return -1

matrix = read_input('puzzle.txt')
result = 0
for i, m in enumerate(matrix):
    result_ = 100 * search_mirror(m, 0)
    if result_ < 0:
        result_ = search_mirror(np.array(m).T, 0)
    result += result_
    

print(result)