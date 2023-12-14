
grids = []
with open("input", "r") as f:
    temp = []
    for line in f.readlines():
        if line == "\n":
            grids.append(temp)
            temp = []
        else:
            temp.append(line.strip())
    grids.append(temp)


def horizontal_reflection(grid):
    for i in range(len(grid) - 1):
        if grid[i] == grid[i + 1]:
            top = i - 1
            bot = i + 2
            match = True
            while top >= 0 and bot < len(grid):
                if grid[top] == grid[bot]:
                    top -= 1
                    bot += 1
                else:
                    match = False
                    break
            if match:
                return i + 1
    return 0

def vertical_reflection(grid):
    for i in range(len(grid[0]) - 1):
        col_left = "".join([grid[j][i] for j in range(len(grid))])
        col_right = "".join([grid[j][i + 1] for j in range(len(grid))])
        if col_left == col_right:
            left = i - 1
            right = i + 2
            match = True
            while left >= 0 and right < len(grid[0]):
                temp_left = "".join([grid[j][left] for j in range(len(grid))])
                temp_right = "".join([grid[j][right] for j in range(len(grid))])
                if temp_left == temp_right:
                    left -= 1
                    right += 1
                else:
                    match = False
                    break
            if match:
                return i + 1
    return 0

curr_sum = 0
for g in grids:
    curr_sum += (100 * horizontal_reflection(g)) + vertical_reflection(g)

print(curr_sum)



