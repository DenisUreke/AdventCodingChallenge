from collections import defaultdict, deque
file_rules = "Advent05_2024.txt"
file_sets = "Advent05_2024_2.txt"


##Topological sort algorithm

class Node():

    def __init__(self, number):
        self.number = number
        self.depends_on = set()
        self.dependants = set()
        self.in_degree = 0
    
    def add_dependancy(self, value):
        """incoming edge to this node."""
        self.depends_on.add(value)
        self.in_degree += 1
    
    def add_dependant_to_this_node(self, value):
        """outgoing edge from this node."""
        self.dependants.add(value)
    
    def remove_dependancy(self):
        self.in_degree -= 1

## make sure None is returned instead of Error if value doesnt exist
nodes = defaultdict(lambda: None)

def create_look_up_list():

    with open(file_rules, "r") as file:
        for rule in file:
            u, v = map(int, rule.split("|"))

            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_dependant_to_this_node(v)
            nodes[v].add_dependancy(u)

def topological_sort():

    queue = deque()
    topological_order = []

    ## .items() is the keyvalue for defaultdict
    for node_number, node in nodes.items():
        if node is not None and node.in_degree == 0:
            queue.append(node_number)

    while(queue):
        current = queue.popleft()
        topological_order.append(current)

        for dependant in nodes[current].dependants:
            nodes[dependant].remove_dependancy()

            if nodes[dependant].in_degree == 0:
                queue.append(dependant)

    # Check for cycles
    if len(topological_order) != len([node for node in nodes.values() if node is not None]):
        raise ValueError("Cycle detected! Topological sorting is not possible.")
    

def start1():
    create_look_up_list()
    topological_sort()

#start()

def read_rules():
    rules_list = defaultdict(list)

    with open(file_rules, "r") as rules:
        for rule in rules:
            first, second = map(int, rule.strip().split("|"))
            rules_list[second].append(first)

    return rules_list
        
def read_list():

    unprocessed = []

    with open(file_sets, "r") as sets:
        for set in sets:
            unprocessed.append(set.strip())

    processed = []

    for line in unprocessed:
        entry = []
        for number in line.split(','):
            entry.append(int(number.strip()))
        processed.append(entry)
    
    return processed

def find_mid_number(current_row):
    # // is integer division
    middle_index = len(current_row) // 2

    return current_row[middle_index]


def compare_list_against_rules(numbers, rules_list):
    count = 0

    for row in numbers:
        passed = True
        for i in range(len(row)):
            current_number = row[i]
            for y in range(i, len(row)):
                if row[y] in rules_list[current_number]:
                    passed = False
                    break
        if passed:
            print(row)
            count += find_mid_number(row)

    return count

def start():
    rules = read_rules()
    list = read_list()
    count = compare_list_against_rules(list, rules)
    print(count)

start()
            












