spelled_numbers = ['one', 'two', 'three', 'four', 'five',
                   'six', 'seven', 'eight', 'nine']


def read_input(file):
    with open(file) as f:
        return f.readlines()


def is_spelled(line, position):
    base = ''.join(line[position:])

    for i, num in enumerate(spelled_numbers):
        if base.startswith(num):
            return True, i+1
    else:
        return False, 0


def get_first_and_last_numbers(line):
    left, right = 0, len(line) -1
    line = list(line)
    number1 = number2 = None

    while (number1 is None or number2 is None):

        candidate1 = is_spelled(line, left)
        if line[left].isdecimal():
            number1 = int(line[left])
        elif candidate1[0]:
            number1 = candidate1[1]
        else:
            left += 1

        candidate2 = is_spelled(line, right)
        if line[right].isdecimal():
            number2 = int(line[right])
        elif candidate2[0]:
            number2 = candidate2[1]
        else:
            right -= 1

    return number1, number2


counter = 0
lines = read_input('input.txt')

for line in lines:
    number1, number2 = get_first_and_last_numbers(line)
    number = int(f'{number1}{number2}')
    counter += number

print(counter)