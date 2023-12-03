
grid = []
with open("input", "r") as f:
    for line in f.readlines():
        grid.append(line.strip())

def in_bounds(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return False
    else:
        return True

part_sum = 0
for i, line in enumerate(grid):
    curr_num = ""
    part_number = False
    for j, c in enumerate(line):
        if c.isnumeric():
            curr_num += c
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if in_bounds(i + ii, j + jj) and not grid[i + ii][j + jj].isnumeric() and grid[i + ii][j + jj] != ".":
                        part_number = True
        else:
            if part_number:
                part_sum += int(curr_num)
            curr_num = ""
            part_number = False
    if part_number:
        part_sum += int(curr_num)

print(part_sum)
