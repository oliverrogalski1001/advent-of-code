
with open("input" , "r") as f:
    lines = f.readlines()
    records = [line.strip().split(" ")[0] for line in lines]
    groups = [[int(x) for x in line.strip().split(" ")[1].split(",")] for line in lines]

mem = {}
for record in records:
    inside = False
    for c in reversed(record):
        if c == "#":
            inside = True


