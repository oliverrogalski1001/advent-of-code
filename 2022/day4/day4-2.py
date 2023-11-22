
with open("input") as f:
    f = f.read().split("\n")

count = 0
for i in f:
    shifts = i.split(",")
    first, second = shifts[0], shifts[1]
    range1 = set(range(int(first[:first.index("-")]), int(first[first.index("-") + 1:]) + 1, 1))
    range2 = set(range(int(second[:second.index("-")]), int(second[second.index("-") + 1:]) + 1, 1))
    if len(range1.intersection(range2)) > 0:
        count += 1

print(count)
