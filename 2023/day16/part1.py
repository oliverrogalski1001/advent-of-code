
with open("input", "r") as f:
    grid = [line.strip() for line in f.readlines()]

def tmul(a, b):
    return a[0] * b, a[1] * b

def split(curr_state):
    dir = curr_state[2]
    r, c = curr_state[:2]
    mirror = grid[r][c]
    if mirror == "|":
        if dir[1]:
            return [(r, c, (1, 0)), (r, c, (-1, 0))]
        else:
            return [(r, c, dir)]
    if mirror == "-":
        if dir[0]:
            return [(r, c, (0, 1)), (r, c, (0, -1))]
        else:
            return [(r, c, dir)]

    mi = 1 if mirror == "\\" else -1
    if dir[1] == 1:
        return [(r, c, tmul((1, 0), mi))]
    if dir[1] == -1:
        return [(r, c, tmul((-1, 0), mi))]
    if dir[0] == 1:
        return [(r, c, tmul((0, 1), mi))]
    if dir[0] == -1:
        return [(r, c, tmul((0, -1), mi))]

def get_line(curr_state):
    dir = curr_state[2]
    r, c = curr_state[:2]
    if dir[0] != 0:
        line = "".join([grid[i][c] for i in range(len(grid))])
    else:
        line = "".join([grid[r][j] for j in range(len(grid[0]))])
    return line

def in_bounds(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def get_next(curr_state):
    dir = curr_state[2]
    dir_i = 1 if dir[0] == 0 else 0
    r, c = curr_state[:2]
    vgrid[r][c] = 1
    if not in_bounds(r, c):
        return
    line = get_line(curr_state)
    pipe_index = c if dir_i else r
    next_pipe = pipe_index
    for i in range(pipe_index + dir[dir_i], -1 if dir[dir_i] == -1 else len(line), dir[dir_i]):
        vgrid[r if dir_i else i][i if dir_i else c] = 1
        if line[i] != ".":
            next_pipe = i
            break
    if next_pipe == pipe_index:
        return
    return next_pipe if not dir_i else r, next_pipe if dir_i else c, dir


starting = []
for i in range(len(grid)):
    starting.append((i, 0, (0, 1)))
    starting.append((i, len(grid[i]) - 1, (0, -1)))

for j in range(len(grid[0])):
    starting.append((0, j, (1, 0)))
    starting.append((len(grid) - 1, j, (-1, 0)))

curr_max = 0
for start in starting:
    energized = 0
    vgrid = [[0] * len(grid[0]) for _ in range(len(grid))]
    stack = [start]
    if grid[start[0]][start[1]] != ".":
        stack += split(stack.pop())
    visited = set()
    while len(stack):
        curr_state = stack.pop()
        if curr_state in visited:
            continue
        visited.add(curr_state)
        next_state = get_next(curr_state)
        if next_state is None:
            continue
        stack += split(next_state)

    curr_max = max(sum([sum(i) for i in vgrid]), curr_max)

print(curr_max)
