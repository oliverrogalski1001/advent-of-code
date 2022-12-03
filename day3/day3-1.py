
with open("input") as f:
    sacks = f.read().split("\n")

points = 0
for sack in sacks:
    a, b = sack[:len(sack) // 2], sack[len(sack) // 2:]
    for i in a:
        if i in b:
            if i.isupper():
                points += ord(i) - 38
            else:
                points += ord(i) - 96
            break

print(points)
