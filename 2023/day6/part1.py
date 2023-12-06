import math

with open("input", "r") as f:
    lines = f.readlines()
    times = [int(x.strip()) for x in lines[0][9:].split(" ") if x != ""]
    distances = [int(x.strip()) for x in lines[1][9:].split(" ") if x != ""]

print(times)
print(distances)

record = 1
for time, distance in zip(times, distances):
    a = math.ceil((-time + math.sqrt((time ** 2) - (4 * distance))) / (2 * -1))
    b = math.floor((-time - math.sqrt((time ** 2) - (4 * distance))) / (2 * -1))
    record *= b - a + 1
print(record)
