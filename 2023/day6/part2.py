import math

with open("input", "r") as f:
    lines = f.readlines()
    times = [x.strip() for x in lines[0][9:] if x.strip() != ""]
    time = int("".join(times))
    distances = [x.strip() for x in lines[1][9:] if x.strip() != ""]
    distance = int("".join(distances))

a = math.ceil((-time + math.sqrt((time ** 2) - (4 * distance))) / (2 * -1))
b = math.floor((-time - math.sqrt((time ** 2) - (4 * distance))) / (2 * -1))
print(b - a + 1)
