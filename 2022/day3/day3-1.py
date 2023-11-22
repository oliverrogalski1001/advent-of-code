
with open("input_test") as f:
    sacks = f.read().split("\n")

points = 0
for sack in sacks:
    a, b = set(sack[:len(sack) // 2]), set(sack[len(sack) // 2:])
    i = a.intersection(b).pop()
    if i.isupper():
        points += ord(i) - 38
    else:
        points += ord(i) - 96

print(points)
