
dirs = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0)
}

def tmul(a, b):
    return a[0] * b, a[1] * b

def tadd(a, b):
    return a[0] + b[0], a[1] + b[1]

with open("input", "r") as f:
    instr = [line.split(" ") for line in f.readlines()]
    instr = list(map(lambda x: (dirs[x[0]], int(x[1])), instr))

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
