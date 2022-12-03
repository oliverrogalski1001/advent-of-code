
with open("input") as f:
    sacks = f.read().split("\n")

points = 0
for i in range(0, len(sacks), 3):
    a, b, c = sacks[i: i + 3]
    char = set(a).intersection(set(b)).intersection(set(c)).pop()
    if char.isupper():
        points += ord(char) - 38
    else:
        points += ord(char) - 96
        
print(points)
