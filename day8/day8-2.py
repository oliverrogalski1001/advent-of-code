
with open("input") as f:
    forest = f.read().split("\n")

size = len(forest)


def check(height, arr):
    count = 0
    for i in arr:
        count += 1
        if i >= height:
            break
    return count


score = 0
for i in range(1, size - 1):
    for j in range(1, size - 1):
        height = forest[i][j]
        left = check(height, reversed(forest[i][:j]))
        right = check(height, forest[i][j + 1:])
        top = check(height, reversed([h[j] for h in forest[:i]]))
        bot = check(height, [h[j] for h in forest[i + 1:]])
        new_score = left * right * top * bot
        score = max(score, new_score)

print(score)
