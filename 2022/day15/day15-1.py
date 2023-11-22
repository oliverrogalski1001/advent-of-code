
with open("input") as f:
    f = f.read().split("\n")

signal = 2000000
cant = set()
for line in f:
    sx, sy = map(lambda x: int(x[x.index("=") + 1:]), line[line.find("x"): line.find(":")].split(", "))
    bx, by = map(lambda x: int(x[x.index("=") + 1:]), line[line.rfind("x"):].split(", "))
    distance = abs(sx - bx) + abs(sy - by)
    if signal in range(sy - distance, sy + distance + 1):
        # print(sx, sy, bx, by, distance)
        for i in range(distance - abs(signal - sy) + 1):
            cant.add(sx + i)
            cant.add(sx - i)
        if by == signal:
            cant.remove(bx)

# print(cant)
print(len(cant))
