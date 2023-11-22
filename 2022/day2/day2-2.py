
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
    p2, outcome = d[a[0]], d[a[1]]
    if outcome == 0:
        p1 = (p2 - 1) % 3
    elif outcome == 1:
        p1 = p2
        points += 3
    else:
        p1 = (p2 + 1) % 3
        points += 6
    points += p1 + 1

print(points)
