import read_txt

def is_number(caracter):
    number = -1

    try:
        number = int(caracter)
    except:
        pass
    return number

def search_numbers(line):

    i = 0
    j = len(line) - 1
    found_solution = False
    first_number, second_number = -1, -1

    while i < len(line) - 1 and j > 0 and not found_solution:
        
        first_number = is_number(line[i])  if first_number == -1 else first_number
        second_number = is_number(line[j]) if second_number == -1 else second_number

        found_solution = True if first_number != -1 and second_number != -1 else False
        i += 1
        j -= 1

    if first_number != -1 and second_number == -1:
        second_number = first_number
    elif first_number == -1 and second_number != -1:
        first_number = second_number

    return int(str(first_number) + str(second_number))

sum = 0
for line in read_txt.contents:
    sum += search_numbers(line)

print(sum)