
with open("input") as f:
    sacks = f.read().split("\n")

points = 0
for i in range(0, len(sacks), 3):
    a, b, c = sacks[i: i + 3]
    print(i, a, b, c)
    for char in a:
        if char in b and char in c:
            print(char)
            if char.isupper():
                points += ord(char) - 38
            else:
                points += ord(char) - 96
            break
print(points)
