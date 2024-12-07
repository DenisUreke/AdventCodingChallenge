file_path = "Advent04_2024.txt"

row_y = []
found = 0

def read_file():

    with open(file_path, "r") as file:

        for line in file:
            column_x = []
            for char in line.strip():
                column_x.append(char)
            row_y.append(column_x)

def check_if_xmas(buffer):
    global found
    left = ""
    right = ""

    left += buffer[0] 
    left += buffer[2]
    left += buffer[4]

    right += buffer[1]
    right += buffer[2]
    right += buffer[3]

    match = ("MAS", "SAM")
    if right in match and left in match:
        found += 1

def check_horisontal():
    y = 0

    while y < len(row_y) -2:
        x = 0
        buffer = ""
        while x < len(row_y[y]) -2:
            buffer = (row_y[y][x], row_y[y][x+2], row_y[y+1][x+1],row_y[y+2][x], row_y[y+2][x+2])
            check_if_xmas(buffer)
            x += 1
        y+= 1




def start():
    read_file()
    check_horisontal()
    print(found)

start()