
with open("input", "r") as f:
    g = [list(line.strip()) for line in f.readlines()]

insert_rows = []
for i, row in enumerate(g):
    if row.count(".") == len(g[0]):
        insert_rows.append(i)

insert_cols = []
for j in range(len(g[0])):
    if [g[i][j] for i in range(len(g))].count(".") == len(g):
        insert_cols.append(j)

nodes = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == "#":
            nodes.append((i, j))

space_factor = 1000000 - 1
paths = 0
for i in range(len(nodes)):
    start_node = nodes[i]
    for j in range(i + 1, len(nodes)):
        end_node = nodes[j]
        space = 0
        for space_row in insert_rows:
            if min(start_node[0], end_node[0]) < space_row < max(start_node[0], end_node[0]):
                space += space_factor
        for space_col in insert_cols:
            if min(start_node[1], end_node[1]) < space_col < max(start_node[1], end_node[1]):
                space += space_factor

        distance = space + abs(start_node[0] - end_node[0]) + abs(start_node[1] - end_node[1])
        paths += distance

print(paths)
