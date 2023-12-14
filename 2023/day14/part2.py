import numpy as np

with open("input_test", "r") as f:
    grid = np.array([[c for c in line.strip()] for line in f.readlines()])

def get_load(g):
    load = 0
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == "O":
                load += len(g) - row
    return load

def cycle(g):
    new_g = np.array([["."] * len(g[0]) for _ in range(len(g))])
    for _ in range(4):
        for col in range(len(g[0])):
            curr_row = 0
            for row in range(len(g)):
                if g[row][col] == "O":
                    new_g[curr_row][col] = "O"
                    curr_row += 1
                if g[row][col] == "#":
                    new_g[row][col] = "#"
                    curr_row = row + 1
        g = np.rot90(new_g, k=-1)
        new_g = np.array([["."] * len(g[0]) for _ in range(len(g))])
    return g


loads = set()
for c in range(1000):
    grid = cycle(grid)
    curr_load = get_load(grid)
    if curr_load in loads:
        print(c)
    else:
        loads.add(get_load(grid))

