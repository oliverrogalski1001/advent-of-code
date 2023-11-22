
with open("input") as f:
    f = f.read().split("\n")

x = 1
cycle = 0
strength = 0

def signal(c, x):
    if c == 20 or (c - 20) % 40 == 0:
        return c * x
    return 0

for i in f:
    cycle += 1
    strength += signal(cycle, x)
    if i[0] == "a":
        cycle += 1
        strength += signal(cycle, x)
        x += int(i.split(" ")[1])

print(strength)