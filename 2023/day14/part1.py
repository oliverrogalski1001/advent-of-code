
with open("input", "r") as f:
    grid = [line.strip() for line in f.readlines()]

def get_load(g):
    load = 0
    for col in range(len(g[0])):
        curr_row = len(g[0])
        for row in range(len(g)):
            if g[row][col] == "O":
                load += curr_row
                curr_row -= 1
            elif g[row][col] == "#":
                curr_row = len(g[0]) - row - 1
    return load

print(get_load(grid))
