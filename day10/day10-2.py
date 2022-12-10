
with open("input") as f:
    f = f.read().split("\n")

draw = []
cycle = 1
x = 1

def check(cycle, x):
    if cycle > 40:
        cycle = 1
    if cycle - 1 in range(x - 1, x + 2):
        draw.append("#")
    else:
        draw.append(".")
    return cycle + 1

def n(cycle, x):
    cycle = check(cycle, x)
    return cycle, x

def a(cycle, x, num):
    cycle = check(cycle, x)
    cycle = check(cycle, x)
    return cycle, x + num

for i in f:
    if i[0] == "n":
        cycle, x = n(cycle, x)
    else:
        cycle, x = a(cycle, x, int(i.split(" ")[1]))

for i, char in enumerate(draw):
    if i % 40 == 0 and i != 0:
        print()
    print(char, end="")

