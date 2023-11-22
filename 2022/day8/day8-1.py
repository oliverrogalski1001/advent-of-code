
with open("input") as f:
    forest = f.read().split("\n")

size = len(forest)
visible = size * 4 - 4


def check(height, arr):
    return len(list(filter(lambda x: x >= height, arr))) == 0


for i in range(1, size - 1):
    for j in range(1, size - 1):
        height = forest[i][j]
        if check(height, forest[i][:j]) or check(height, forest[i][j + 1:]) or \
                check(height, [h[j] for h in forest[:i]]) or check(height, [h[j] for h in forest[i + 1:]]):
            visible += 1

print(visible)
