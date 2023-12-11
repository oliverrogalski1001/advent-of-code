import math

with open("input", "r") as f:
    lines = f.readlines()
    times = [int(x.strip()) for x in lines[0][9:].split(" ") if x != ""]
    distances = [int(x.strip()) for x in lines[1][9:].split(" ") if x != ""]

record = 1
for time, distance in zip(times, distances):
    a = math.ceil((-time + math.sqrt((time ** 2) - (4 * distance))) / (2 * -1))
    b = math.floor((-time - math.sqrt((time ** 2) - (4 * distance))) / (2 * -1))
    print(b, a)
    offset = 1
    if (time * a) - (a**2) == distance:
        offset -= 1
    if (time * b) - (b**2) == distance:
        offset -= 1
    record *= b - a + offset

print(record)
