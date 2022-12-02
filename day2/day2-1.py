
with open("input") as f:
    plan = f.read()

d = {"A": 0,
     "B": 1,
     "C": 2,
     "X": 0,
     "Y": 1,
     "Z": 2}

points = 0
for line in plan.split("\n"):
    a = line.split(" ")
    p2, p1 = d[a[0]], d[a[1]]
    points += p1 + 1
    if (p1 - 1) % 3 == p2:
        points += 6
    elif p1 == p2:
        points += 3

print(points)
