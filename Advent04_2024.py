file_path = "Advent04_2024.txt"

row_y = []
found = 0

class Letter():

    def __init__(self, letter = "", is_used = False):
        self.letter = letter
        self.is_used = is_used

class Buffer():

    def __init__(self, buffer = "" ):
        self.letters_and_boolean = []
        self.buffer = buffer

def read_file():

    with open(file_path, "r") as file:

        for line in file:
            column_x = []
            for char in line.strip():
                new_letter = Letter(letter= char)
                column_x.append(new_letter)
            row_y.append(column_x)

def check_if_atleast_one_letter_is_unused(list):
    
    for object in list:
        if not object[2]:
            return True
    
    return False

def adjust_the_list(in_list):

    for object in in_list:
        row_y[object[0]][object[1]].is_used = True

def check_if_christmas(buffer):
    global found

    word = buffer.buffer
    valid_words = ["XMAS", "SAMX"]
    if word in valid_words:
        if check_if_atleast_one_letter_is_unused(buffer.letters_and_boolean):
            found += 1
            adjust_the_list(buffer.letters_and_boolean)

def check_vertical():
    buffer = Buffer() 
    x = 0

    while x < len(row_y[0]):
        y = 0
        buffer.buffer = ""
        buffer.letters_and_boolean = []
        while y < len(row_y):
            buffer.buffer += row_y[y][x].letter
            coordinates = (y, x, row_y[y][x].is_used) 
            buffer.letters_and_boolean.append(coordinates)
            if len(buffer.buffer) == 4:
                check_if_christmas(buffer=buffer)
                buffer.buffer = buffer.buffer[1:]
                buffer.letters_and_boolean.pop(0)
            y += 1
        x += 1


def check_horisontal():
    buffer = Buffer() 
    y = 0

    while y < len(row_y):
        x = 0
        buffer.buffer = ""
        buffer.letters_and_boolean = []
        while x < len(row_y[y]):
            buffer.buffer += row_y[y][x].letter
            coordinates = (y, x, row_y[y][x].is_used)
            buffer.letters_and_boolean.append(coordinates)
            if len(buffer.buffer) == 4:
                check_if_christmas(buffer=buffer)
                buffer.buffer = buffer.buffer[1:]
                buffer.letters_and_boolean.pop(0)
            x += 1
        y += 1

def check_diagonal_top_left_right_down():
    buffer = Buffer()
    for start_row in range(len(row_y)):
        x, y = 0, start_row
        buffer.buffer = ""
        buffer.letters_and_boolean = []
        while x < len(row_y[0]) and y < len(row_y):
            buffer.buffer += row_y[y][x].letter
            coordinates = (y, x, row_y[y][x].is_used)
            buffer.letters_and_boolean.append(coordinates)
            if len(buffer.buffer) == 4:
                check_if_christmas(buffer=buffer)
                buffer.buffer = buffer.buffer[1:]
                buffer.letters_and_boolean.pop(0)
            x += 1
            y += 1

    for start_col in range(1, len(row_y[0])):
        x, y = start_col, 0
        buffer.buffer = ""
        buffer.letters_and_boolean = []
        while x < len(row_y[0]) and y < len(row_y):
            buffer.buffer += row_y[y][x].letter
            coordinates = (y, x, row_y[y][x].is_used)
            buffer.letters_and_boolean.append(coordinates)
            if len(buffer.buffer) == 4:
                check_if_christmas(buffer=buffer)
                buffer.buffer = buffer.buffer[1:]
                buffer.letters_and_boolean.pop(0)
            x += 1
            y += 1

def check_diagonal_top_right_left_down():
    buffer = Buffer()
    for start_row in range(len(row_y)):
        x, y = len(row_y[0]) - 1, start_row
        buffer.buffer = ""
        buffer.letters_and_boolean = []
        while x >= 0 and y < len(row_y):
            buffer.buffer += row_y[y][x].letter
            coordinates = (y, x, row_y[y][x].is_used)
            buffer.letters_and_boolean.append(coordinates)
            if len(buffer.buffer) == 4:
                check_if_christmas(buffer=buffer)
                buffer.buffer = buffer.buffer[1:]
                buffer.letters_and_boolean.pop(0)
            x -= 1
            y += 1

    for start_col in range(len(row_y[0]) - 2, -1, -1):
        x, y = start_col, 0
        buffer.buffer = ""
        buffer.letters_and_boolean = []
        while x >= 0 and y < len(row_y):
            buffer.buffer += row_y[y][x].letter
            coordinates = (y, x, row_y[y][x].is_used)
            buffer.letters_and_boolean.append(coordinates)
            if len(buffer.buffer) == 4:
                check_if_christmas(buffer=buffer)
                buffer.buffer = buffer.buffer[1:]
                buffer.letters_and_boolean.pop(0)
            x -= 1
            y += 1

def check_diagonal_top_left_right_down():
    buffer = Buffer()
    y = 0

def start():
    read_file()
    check_horisontal()
    check_vertical()
    check_diagonal_top_left_right_down()
    check_diagonal_top_right_left_down()
    print(found)

start()



            

    



