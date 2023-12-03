
grid = []
with open("input_test", "r") as f:
    for line in f.readlines():
        grid.append(line.strip())

def in_bounds(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return False
    else:
        return True

num_coords = {}
for i, line in enumerate(grid):
    curr_num = ""
    part_number = False
    nums = []
    for j, c in enumerate(line):
        if c.isnumeric():
            curr_num += c
            nums.append((i, j))
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if in_bounds(i + ii, j + jj) and not grid[i + ii][j + jj].isnumeric() and grid[i + ii][j + jj] != ".":
                        part_number = True
        else:
            if part_number:
                for coord in nums:
                    num_coords[coord] = int(curr_num)
            nums.clear()
            curr_num = ""
            part_number = False
    if part_number:
        for coord in nums:
            num_coords[coord] = int(curr_num)

print(num_coords)

for i, line in enumerate(grid):
    for j, c in enumerate(line):

            for ii in range(-1, 2):
                for jj in range(-1, 2):

