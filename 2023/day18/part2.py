
dirs = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}

def tmul(a, b):
    return a[0] * b, a[1] * b

def tadd(a, b):
    return a[0] + b[0], a[1] + b[1]

with open("input", "r") as f:
    instr = [line.split(" ")[2].strip()[2:8] for line in f.readlines()]
    instr = list(map(lambda x: (dirs[int(x[5])], int(x[:5], base=16)), instr))

v = [(0, 0)]
curr_coords = (0, 0)
b = 0
for ins in instr:
    curr_coords = tadd(curr_coords, tmul(ins[0], ins[1]))
    v.append(curr_coords)
    b += ins[1]

area = 0
for i in range(len(v) - 1):
    area += (v[i][1] - v[i + 1][1]) * (v[i][0] + v[i + 1][0])
area = (area // 2) + (b // 2) + 1

print(area)
