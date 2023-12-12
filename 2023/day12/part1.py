
with open("input" , "r") as f:
    lines = f.readlines()
    records = [line.strip().split(" ")[0] for line in lines]
    groups = [[int(x) for x in line.strip().split(" ")[1].split(",")] for line in lines]

def check(rec, g):
    return [len(x) for x in rec.split(".") if x != ""] == g

def gen_rec(curr_rec, g):
    if curr_rec.count("?") == 0:
        return check(curr_rec, g)
    next_q = curr_rec.index("?")
    return gen_rec(curr_rec[:next_q] + "#" + curr_rec[next_q + 1:], g) + gen_rec(curr_rec[:next_q] + "." + curr_rec[next_q + 1:], g)


arrange_sum = 0
for record, group in zip(records, groups):
    arrange_sum += gen_rec(record, group)

print(arrange_sum)

