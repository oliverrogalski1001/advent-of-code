
with open("input") as f:
    f = f.read().split("\n\n")


def compare_lists(l, r):
    for val in range(min(len(l), len(r))):
        left, right = l[val], r[val]
        if type(left) is list and type(right) is list:
            inner_list = compare_lists(left, right)
            if type(inner_list) is bool:
                return inner_list
            continue
        elif type(left) is int and type(right) is list:
            inner_list = compare_lists([left], right)
            if type(inner_list) is bool:
                return inner_list
            continue
        elif type(left) is list and type(right) is int:
            inner_list = compare_lists(left, [right])
            if type(inner_list) is bool:
                return inner_list
            continue

        if left < right:
            return True
        elif left > right:
            return False

    if len(l) == len(r):
        return 0
    return len(l) < len(r)


count = 0
lines = [[[2]], [[6]]]
for line in f:
    l, r = line.split("\n")
    l, r = eval(l), eval(r)
    lines.extend([l, r])

sort = False
while not sort:
    sort = True
    for i in range(len(lines) - 1):
        if not compare_lists(lines[i], lines[i + 1]):
            lines[i], lines[i + 1] = lines[i + 1], lines[i]
            sort = False

print((lines.index([[6]]) + 1) * (lines.index([[2]]) + 1))
