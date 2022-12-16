
with open("input") as f:
    f = f.read().split("\n")

sb = {}
for line in f:
    sx, sy = map(lambda x: int(x[x.index("=") + 1:]), line[line.find("x"): line.find(":")].split(", "))
    bx, by = map(lambda x: int(x[x.index("=") + 1:]), line[line.rfind("x"):].split(", "))
    distance = abs(sx - bx) + abs(sy - by)
    sb[(sx, sy)] = distance

limit = 4000000
bounds = {}
for scanner in sb.keys():
    distance = sb[scanner] + 1
    print(f"scanner {scanner[0]}, {scanner[1]}, distance: {distance}")
    for i in range(-distance, distance + 1):
        bx = scanner[0] + i
        byp = scanner[1] + (distance - abs(i))
        byn = scanner[1] - (distance - abs(i))
        if bx not in range(0, limit + 1) or byp not in range(0, limit + 1):
            continue
        if bx not in range(0, limit + 1) or byn not in range(0, limit + 1):
            continue

        if (bx, byp) in bounds.keys():
            bounds[(bx, byp)] += 1
        else:
            bounds[(bx, byp)] = 1

        if (bx, byn) in bounds.keys():
            bounds[(bx, byn)] += 1
        else:
            bounds[(bx, byn)] = 1

for count in bounds.keys():
    if bounds[count] == 4:
        print(count[0] * 4000000 + count[1])


