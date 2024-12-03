
file_path = 'test.txt'
lines = ''
safe_reports = 0

class Value:
    def __init__(self, value=0, is_ascending=False, is_equal_value = False):
        self.value = value
        self.is_ascending = is_ascending
        self.is_equal_value = is_equal_value

class Value_List:
    def __init__(self):
        self.values = []
        self.clipped = 0
        self.ascending = False
        self.still_ok = True

    def add_value(self, value = 0, is_ascending = False, is_equal_value = False):
        self.values.append(Value(value=value, is_ascending=is_ascending, is_equal_value= is_equal_value ))


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

def prepare_list_direction(integers):

    value_list = Value_List()

    if integers[0] > integers[1]:
        value_list.add_value(value=integers[0], is_ascending= False)
    else:
        value_list.add_value(value=integers[0], is_ascending= True)

    for i in range(len(integers) -1):
        if integers[i] == integers[i + 1]:
            value_list.add_value(value= integers[i + 1], is_equal_value= True )
        elif integers[i] < integers[i + 1]:
            value_list.add_value(value= integers[i + 1], is_ascending= True)
        else:
            value_list.add_value(value= integers[i + 1], is_ascending= False)

    return value_list

def check_how_many_equal_values(values_list):
    count = 0

    for value in values_list.values:
        if value.is_equal_value:
            count += 1
    
    return count <= 1

def remove_duplicate(values_list):

    i = 0
    while i < len(values_list.values):
        if values_list.values[i].is_equal_value:
            del values_list.values[i]
            values_list.clipped += 1
        else:
            i += 1 

    return values_list

def remove_value_with_wrong_direction(values_list, isAscending):

    i = 0
    while i < len(values_list.values):
        if values_list.values[i].is_ascending != isAscending:
            del values_list.values[i]
            values_list.clipped += 1
        else:
            i += 1 

    return values_list


def check_direction_of_values(values_list):
    ascending = 0
    descending = 0

    for value in values_list.values:
        if value.is_ascending:
            ascending += 1
        elif not value.is_ascending:
            descending += 1

    if ascending > descending:
        values_list.ascending = True
    else:
        values_list.ascending = False
    
    values_list = remove_value_with_wrong_direction(values_list=values_list, isAscending= values_list.ascending)

    return values_list
    
def check_range(value_1, value_2):
    absolute_value = abs(value_1 - value_2)
    return 1 <= absolute_value <= 3

def check_if_range_is_ok(values_list):

    for i in range(len(values_list.values)):
    
        if(i == len(values_list.values) -1):
            return True
        elif not check_range(values_list.values[i].value, values_list.values[i + 1].value):
            return False


def check_rules(values_list):
    global safe_reports

    values_list = remove_duplicate(values_list)
    values_list = check_direction_of_values(values_list)
    print([value.value for value in values_list.values])
    if values_list.clipped < 2 and check_if_range_is_ok(values_list):
        safe_reports += 1


def start_check():
    read_file()
    for i in range(len(lines)):
        integers_list =  extract_integers_from_line(i)
        values_list = prepare_list_direction(integers_list)
        print([value.value for value in values_list.values])
        check_rules(values_list)
        print(f"Clipped = {values_list.clipped}")


start_check()
print(safe_reports)