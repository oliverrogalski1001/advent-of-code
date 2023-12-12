from functools import cache

with open("input", "r") as f:
    lines = f.readlines()
    records = [((line.strip().split(" ")[0] + "?") * 5)[:-1] for line in lines]
    groups = [[int(x) for x in line.strip().split(" ")[1].split(",") * 5] for line in lines]
    groups = [tuple(g) for g in groups]

@cache
def gen_rec(rec, group):
    if rec == "":
        return 1 if group == () else 0
    if group == ():
        return 1 if "#" not in rec else 0

    curr_sum = 0
    if rec[0] == "#" or rec[0] == "?":
        if len(rec) >= group[0] and "." not in rec[:group[0]] and (group[0] >= len(rec) or rec[group[0]] in "?."):
            curr_sum += gen_rec(rec[group[0] + 1:], group[1:])

    if rec[0] == "." or rec[0] == "?":
        curr_sum += gen_rec(rec[1:], group)

    return curr_sum

arrange_sum = 0
for record, group in zip(records, groups):
    arrange_sum += gen_rec(record, group)

print(arrange_sum)


