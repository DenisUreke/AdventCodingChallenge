import re

file_path = "Advent03_2024.txt"

pattern = r"mul\((\d+),(\d+)\)"
find_whole = r"mul\(\d+,\d+\)"
do = r"do\(\)"
dont = r"don't\(\)"

combined_pattern = f"({find_whole})|({do})|({dont})"

def read_list():
    matches = []
    with open(file_path, "r") as file:
        for line in file:
            for match in re.finditer(combined_pattern, line):
                match_text = match.group(0)
                matches.append(match_text)
    return matches


def calculate(list):
    is_calculate = True
    summary = 0

    for entry in list:
        if re.fullmatch(do, entry):
            is_calculate = True
            continue
        elif re.fullmatch(dont, entry):
            is_calculate = False
            continue
        if re.fullmatch(find_whole, entry) and is_calculate:
             values = re.fullmatch(pattern, entry)
             x, y = int(values.group(1)), int(values.group(2))
             summary += x * y

    return summary

def start():
    matches = read_list()
    summary = calculate(matches)
    print(summary)

start()



    