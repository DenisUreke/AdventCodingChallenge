
file_path = 'Advent02_2024.txt'
lines = ''
safe_reports = 0

def read_file():
    global lines
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]

def extract_integers_from_line(index):
    integers = []

    integers = [int(num) for num in lines[index].split()]

    return integers

def check_range(value_1, value_2):
    absolute_value = abs(value_1 - value_2)
    return 1 <= absolute_value <= 3

def check_rules(integers):
    global safe_reports

    isAscending = True if integers[0] < integers[1] else False

    for i in range(len(integers)):
    
        if(i == len(integers) -1):
            safe_reports += 1
            return
        
        if isAscending == True:
            if integers[i] < integers[i + 1] and check_range(integers[i], integers[i + 1]):
                continue
            else:
                break
        if isAscending == False:
            if integers[i] > integers[i + 1] and check_range(integers[i], integers[i + 1]):
                continue
            else:
                break

def start_check():

    for i in range(len(lines)):
        integers_list =  extract_integers_from_line(i)
        check_rules(integers_list)



read_file()
start_check()
print(safe_reports)







