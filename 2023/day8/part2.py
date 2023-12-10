from functools import reduce

network = {}
starting_nodes = []
with open("input", "r") as f:
    directions = f.readline().strip()
    directions = directions.replace("L", "0")
    directions = directions.replace("R", "1")
    f.readline()
    for line in f.readlines():
        network[line[:3]] = (line[7:10], line[12:15])
        if line[2] == "A":
            starting_nodes.append(line[:3])

total_steps = []
for curr_node in starting_nodes:
    steps = 0
    curr_dir_index = 0
    while curr_node[2] != "Z":
        direction = int(directions[curr_dir_index])
        curr_node = network[curr_node][direction]
        steps += 1
        curr_dir_index += 1
        curr_dir_index = curr_dir_index % len(directions)
    total_steps.append(steps)

def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)

def lcm(x, y):
    return (x * y) // gcd(x, y)

print(reduce(lcm, total_steps))
