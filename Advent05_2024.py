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
'''nodes = defaultdict(lambda: None)

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
    topological_sort()'''

#start()

###############################################################################

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
    errors_list = []

    for row in numbers:
        passed = True
        for i in range(len(row)):
            if not passed:
                break
            current_number = row[i]
            for y in range(i, len(row)):
                if row[y] in rules_list[current_number]:
                    errors_list.append(row)
                    passed = False
                    break
        if passed:
            count += find_mid_number(row)

    return count, errors_list

def topological_sort(nodes):

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
    
    return topological_order

def create_topological_list_for_errors(rules_list, error_list):
    #if is in list that is sent in and in the dependencies list then we know

    nodes = defaultdict(Node)

    for entry in error_list:
        for value in entry:
            if value not in nodes:
                nodes[value] = Node(value)
            
            dependants = rules_list[value]

            for dependant in dependants:
                if dependant in entry:

                    if dependant not in nodes:
                        nodes[dependant] = Node(dependant)

                        nodes[value].add_dependancy(dependant)
                        nodes[dependant].add_dependant_to_this_node(value)

    return nodes

def sort_by_predefined_order(predefined_order, input_list):

    order_mapping = {number: index for index, number in enumerate(predefined_order)}
    return sorted(input_list, key=lambda x: order_mapping.get(x, float('inf')))


def start():
    the_value = 0
    rules = read_rules()
    list = read_list()
    count, errors_list = compare_list_against_rules(list, rules)
    nodes = create_topological_list_for_errors(rules, errors_list)
    order = topological_sort(nodes)
    sorted_list = [sort_by_predefined_order(order, entry) for entry in errors_list]
    
    for entry in sorted_list:
        mid_number = find_mid_number(entry)
        print(f"Middle Number for {entry}: {mid_number}")
        the_value += mid_number
        print(f"Updated Count: {count}")
        
    print(the_value)


    #for idx, entry in enumerate(sorted_list):
        #print(f"Sorted Entry {idx + 1}: {entry}")

start()
            












