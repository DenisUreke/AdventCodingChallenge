import re

file_path = "Advent03_2024.txt"

find_whole = r"mul\(\d+,\d+\)"
pattern = r"mul\((\d+),(\d+)\)"

with open(file_path, 'r') as file:
    text = file.read() 

matches = re.findall(find_whole, text)

cleaned = []
for match in matches:
    cleaned.extend(re.findall(pattern, match))

total = 0
for match in cleaned:
    first_number, second_number = map(int, match) # DUH!
    product = first_number * second_number
    total += product

print(total)