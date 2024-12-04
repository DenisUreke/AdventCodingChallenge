file_path = "Advent04_2024.txt"

row_y = []
found = 0

class Letter():

    def __init__(self, letter = "", is_used = False):
        self.letter = letter
        self.is_used = is_used


def read_file():

    with open(file_path, "r") as file:

        for line in file:
            column_x = []
            for char in line.strip():
                new_letter = Letter(letter= char)
                column_x.append(new_letter)
            row_y.append(column_x)

def adjust_list(y, x):

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
            adjust_list(y,x)



def check_horisontal():

    buffer = ""
    x = 0
    y = 0

    while( y < len(row_y)):
        while( x < len(row_y[y])):
            buffer = row_y[y][x].letter
            x += 1
    y += 1


            

    



