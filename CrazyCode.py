##Brutenis Gliwa wrote this code
## https://github.com/LiquidFun

file_path = "Advent04_2024.txt"

# Read the file content into a list of rows
with open(file_path, "r") as file:
    grid = [line.strip() for line in file]

# Create the coordinates dictionary from the grid
coords = {x + 1j * y: c for y, r in enumerate(grid) for x, c in enumerate(r)}

# Function to get character at a coordinate or default to an empty string
g = lambda c: coords.get(c, "")

# Initialize counters
s1 = s2 = 0

# Check all directions
for c in coords:
    for d in [1, 1j, 1+1j, 1-1j, -1, -1j, -1+1j, -1-1j]:
        # Count full "XMAS" matches
        s1 += g(c) + g(c+d) + g(c+d*2) + g(c+d*3) == "XMAS"
        
        # Count partial matches for diagonals
        if d.imag and d.real:  # Diagonal directions only
            s2 += g(c+d) + g(c) + g(c-d) == "MAS" and g(c+d*1j) + g(c-d*1j) == "MS"

# Print the results
print(s1, s2, sep="\n")




###-------------------------

class Node:
    def __init__(self, number):
        self.number = number          # The page number
        self.depends_on = set()       # Numbers this node depends on (incoming edges)
        self.dependents = set()       # Numbers that depend on this node (outgoing edges)
        self.in_degree = 0            # Number of prerequisites (incoming edges)

    def add_dependency(self, prerequisite):
        """Adds a prerequisite (incoming edge) to this node."""
        self.depends_on.add(prerequisite)
        self.in_degree += 1

    def add_dependent(self, dependent):
        """Adds a dependent (outgoing edge) to this node."""
        self.dependents.add(dependent)

    def remove_dependency(self):
        """Removes a dependency (used in Kahn's algorithm to update in-degrees)."""
        self.in_degree -= 1


    from collections import defaultdict

# Parse the rules
rules = ["95|92", "19|26", "19|94", "19|92", "19|64", "52|29", "52|74", "52|86"]

# Create a dictionary to hold Node objects
nodes = defaultdict(Node)

for rule in rules:
    u, v = map(int, rule.split('|'))
    
    # Ensure both nodes exist in the dictionary
    if u not in nodes:
        nodes[u] = Node(u)
    if v not in nodes:
        nodes[v] = Node(v)
    
    # Add dependencies and dependents
    nodes[u].add_dependent(v)
    nodes[v].add_dependency(u)