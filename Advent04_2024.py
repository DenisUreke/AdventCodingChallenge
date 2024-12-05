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

def adjust_list_horisontal(y, x):

    column = x
    while (column < x + 4):
        row_y[y][column].is_used = True
        column += 1

def check_if_on_is_unused(y, x):

    column = x
    while (column < x + 4):
        if not row_y[y][column].is_used:
            return True
        column += 1

    return False
    

def check_if_xmas(buffer, y, x):
    global found

    if buffer == "XMAS" or buffer == "SAMX":
        if(check_if_on_is_unused(y, x)):
            found += 1
            adjust_list_horisontal(y,x)

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

    if buffer.buffer == "XMAS" or buffer.buffer == "SAMX":
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
                buffer.buffer = ""
                buffer.letters_and_boolean = []
            y += 1
        x += 1


def check_horisontal():
    buffer = ""
    y = 0

    while y < len(row_y):
        x = 0
        while x < len(row_y[y]):
            buffer += row_y[y][x].letter
            if len(buffer) == 4:
                check_if_xmas(buffer=buffer, y=y, x=x - 3)
                buffer = ""
            x += 1
        y += 1

def start():
    read_file()
    check_horisontal()
    #check_vertical()
    print(found)

start()



            

    



