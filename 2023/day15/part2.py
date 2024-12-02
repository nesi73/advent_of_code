
def initialize_boxes(number):
    boxes = []
    for i in range(number):
        boxes.append({})
    return boxes

def read_file(path):
    file = open(path).read().strip()
    return file.split(',')

def calculate_HASH(ascii_values):
    current_value = 0

    for value in ascii_values:
        current_value = (current_value + value) * 17 % 256
    return current_value

def get_ASCII(_str):
    ascii_values = []
    for char in _str:
        ascii_values.append(ord(char))
    
    return ascii_values

def compute_boxes(label_complete, boxes):
    operation = "=" if "=" in label_complete else "-"
    
    if operation == "=":
        label = label_complete.split("=")[0]
        focal_length = label_complete.split("=")[1]
        current_box = calculate_HASH(get_ASCII(label))

        if label in boxes[current_box]:
            boxes[current_box][label] = focal_length
        else:
            boxes[current_box].update({label : focal_length})
    else:
        label = label_complete.split("-")[0]
        current_box = calculate_HASH(get_ASCII(label))

        if label in boxes[current_box]:
            del boxes[current_box][label]

def focusing_power(boxes):
    solution = 0
    for id_box, box in enumerate(boxes):
        if len(box) == 0:
            continue
        
        for id_lens, lens in enumerate(box):
            solution += (id_box + 1) * (id_lens + 1) * int(box[lens])
    return solution

import sys

lines = read_file(sys.argv[1])
boxes = initialize_boxes(256)

for line in lines:
    compute_boxes(line, boxes)

print(focusing_power(boxes))
