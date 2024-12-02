import re
file_path = 'AdventText03.txt'

lines = ''
summary = 0


def read_file():
    global lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

def check_after(y, x):
    index = x

    while True:
        lines[y][index]
        if lines[y][index] != '.' and not lines[y][index].isdigit(): 
            return True
        elif lines[y][index] == '.':
            return False
        if index < len(lines[y]):
            index += 1
            continue
        else:
            return False

def check_before(y,x):

    if x == 0:
        return
    index = x

    if lines[y][index-1] != '.' and not lines[y][index -1].isdigit():
        return True
    else: 
        return False
    
def extract_value(y, x):
    found_value_as_string = ''
    index = x

    while True:
        if not lines[y][index].isdigit():
            return found_value_as_string
        elif index == len(lines[y]):
            return found_value_as_string    
        else:
            found_value_as_string += lines[y][index]
            index += 1
            #print(lines[y][index])

def check_over_under(y,x, length):

    if y > 0:
        for i in range(length):
            if lines[y-1][x+i] != '.' and not lines[y-1][x+i].isdigit():
                return True
    if y < len(lines) -1:
        for i in range(length):
            if lines[y+1][x+i] != '.' and not lines[y+1][x+i].isdigit():
                return True
            
    return False

def digit_found(y, x):
    global summary
    found_value = ''
    
    found_value = extract_value(y,x)

    if check_over_under(y,x, len(found_value)) or check_before(y, x) or check_after(y, x):
        summary += int(found_value)





def add_keys():
    global lines

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x].isdigit():
                print(lines[y][x])
                digit_found(y,x)





read_file()
add_keys()
print(summary)