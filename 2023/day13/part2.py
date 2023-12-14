
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

print(grids)

def horizontal_reflection(grid):
    for i in range(len(grid) - 1):
        if diff(grid[i], grid[i + 1]) <= 1:
            top = i - 1
            bot = i + 2
            match = True
            temp_top = grid[i]
            temp_bot = grid[i + 1]
            while top >= 0 and bot < len(grid):
                temp_top += grid[top]
                temp_bot += grid[bot]
                if diff(temp_top, temp_bot) <= 1:
                    top -= 1
                    bot += 1
                else:
                    match = False
                    break
            if match and diff(temp_top, temp_bot) == 1:
                return i + 1
    return 0

def vertical_reflection(grid):
    for i in range(len(grid[0]) - 1):
        col_left = "".join([grid[j][i] for j in range(len(grid))])
        col_right = "".join([grid[j][i + 1] for j in range(len(grid))])
        if diff(col_left, col_right) <= 1:
            left = i - 1
            right = i + 2
            match = True
            temp_left = col_left
            temp_right = col_right
            while left >= 0 and right < len(grid[0]):
                temp_left += "".join([grid[j][left] for j in range(len(grid))])
                temp_right += "".join([grid[j][right] for j in range(len(grid))])
                if diff(temp_left, temp_right) <= 1:
                    left -= 1
                    right += 1
                else:
                    match = False
                    break
            if match and diff(temp_left, temp_right) == 1:
                return i + 1
    return 0

def diff(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d


curr_sum = 0
for g in grids:
    h_r = horizontal_reflection(g)
    v_r = vertical_reflection(g)
    curr_sum += (100 * h_r) + v_r

print(curr_sum)
