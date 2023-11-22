from collections import deque

with open("input") as f:
    f = f.read().split("\n\n")

crates = f[0]
levels = crates.split("\n")
q = {}
num = 1
for i in range(1, len(levels[-1]), 4):
    q[num] = deque()
    for j in range(len(levels) - 1):
        try:
            crate = levels[j][i]
            if not crate.strip():
                continue
            q[num].append(levels[j][i])
        except IndexError:
            continue
    num += 1
instructions = f[1].split("\n")

for i in instructions:
    move, begin, to = map(int, filter(lambda x: x.isnumeric(), i.split(" ")))
    slice = list(q[begin])[:move]
    for j in range(move):
        q[begin].popleft()
    slice.reverse()
    q[to].extendleft(slice)

result = "".join([q[i + 1].popleft() for i in range(len(q))])

print(result)
