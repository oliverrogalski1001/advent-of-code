
with open("input") as f:
    f = f.read().split("\n")

count = 0
for i in f:
    shifts = i.split(",")
    first, second = shifts[0], shifts[1]
    range1 = set(range(int(first[:first.index("-")]), int(first[first.index("-") + 1:]) + 1, 1))
    range2 = set(range(int(second[:second.index("-")]), int(second[second.index("-") + 1:]) + 1, 1))
    union = range1.union(range2)
    if union == range1 or union == range2:
        count += 1

print(count)
