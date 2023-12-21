
with open("input_test", "r") as f:
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

    mi = 1 if mirror == r"\"" else -1
    if dir[1] == 1:
        return [(r, c, tmul((1, 0), mi))]
    if dir[1] == -1:
        return [(r, c, tmul((0, -1), mi))]
    if dir[0] == 1:
        return [(r, c, tmul((0, 1), mi))]
    if dir[0] == -1:
        return [(r, c, tmul((-1, 0), mi))]

def get_line(curr_state):
    dir = curr_state[2]
    r, c = curr_state[:2]
    if dir[0] != 0:
        line = "".join([grid[i][c] for i in range(len(grid))])
    else:
        line = "".join([grid[r][j] for j in range(len(grid[0]))])
    print(line)
    return line

def get_next(curr_state):
    dir = curr_state[2]
    dir_i = 1 if dir[0] == 0 else 0
    r, c = curr_state[:2]
    line = get_line(curr_state)
    pipe_index = c if dir_i else r
    next_pipe = pipe_index
    for i in range(pipe_index + dir[dir_i], -1 if dir[dir_i] == -1 else len(line), dir[dir_i]):
        if line[i] != ".":
            next_pipe = i
            break
    if next_pipe == pipe_index:
        next_pipe = len(line) - 1
    return next_pipe if not dir_i else r, next_pipe if dir_i else c, dir

energized = 0
stack = [(0, 5, (0, -1))]
while len(stack):
    curr_state = stack.pop()
    next_state = get_next(curr_state)
    print(next_state)
    print(split(next_state))
