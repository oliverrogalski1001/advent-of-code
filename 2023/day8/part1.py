
network = {}
with open("input", "r") as f:
    directions = f.readline().strip()
    directions = directions.replace("L", "0")
    directions = directions.replace("R", "1")
    f.readline()
    for line in f.readlines():
        network[line[:3]] = (line[7:10], line[12:15])

curr_node = "AAA"
steps = 0
curr_dir_index = 0
while curr_node != "ZZZ":
    direction = int(directions[curr_dir_index])
    curr_node = network[curr_node][direction]
    steps += 1
    curr_dir_index += 1
    curr_dir_index = curr_dir_index % len(directions)

print(steps)
