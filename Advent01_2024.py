'''ownerproof-4438009-1733095176-e04c08a55037'''

import re
file_path = 'Adventure01_2024.txt'

list_a = []
list_b = []


def read_list():

    with open(file_path, 'r') as file:
        for line in file:

            values = line.split()
            if len(values) == 2:
                list_a.append(int(values[0]))
                list_b.append(int(values[1]))
        list_a.sort()
        list_b.sort()


def compare_lists():

    summary = 0

    for item_a, item_b in zip(list_a, list_b):

        summary += abs(item_a - item_b)

    return summary



def similarity_list():
    summary = 0

    for entry_a in list_a:
        multiplier = 0
        for entry_b in list_b:
            if(entry_a == entry_b):
                multiplier += 1
        summary += (entry_a * multiplier)

    return summary


read_list()
#print(compare_lists())
print(similarity_list())
