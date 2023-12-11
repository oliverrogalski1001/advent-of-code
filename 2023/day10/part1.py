
with open("input", "r") as f:
    grid = [line.strip() for line in f.readlines()]


def get_start(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(grid[i]):
            if grid[i][j] == "S":
                return i, j

start_r, start_c = get_start(grid)

connect = {
    ("|", 1, 0): (-1, 0),
    ("|", -1, 0): (1, 0),
    ("-", 0, 1): (0, -1),
    ("-", 0, -1): (0, 1),
    ("L", -1, 0): (0, 1),
    ("L", 0, 1): (-1, 0),
    ("J", -1, 0): (0, -1),
    ("J", 0, -1): (-1, 0),
    ("7", 0, -1): (1, 0),
    ("7", 1, 0): (0, -1),
    ("F", 1, 0): (0, 1),
    ("F", 0, 1): (1, 0)
}

def next_dir(from_r, from_c, r, c):
    curr_pipe = grid[r][c]
    return connect[(curr_pipe, from_r, from_c)]


dy, dx = 0, 1
curr_r, curr_c = start_r + dy, start_c + dx
count = 1
while curr_r != start_r or curr_c != start_c:
    dy, dx = next_dir(-dy, -dx, curr_r, curr_c)
    curr_r += dy
    curr_c += dx
    count += 1

print(count // 2)
