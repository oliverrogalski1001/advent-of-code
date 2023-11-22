
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
for i, line in enumerate(f):
    l, r = line.split("\n")
    l, r = eval(l), eval(r)
    if compare_lists(l, r):
        count += i + 1

print(count)
