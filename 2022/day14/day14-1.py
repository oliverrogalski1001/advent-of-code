
with open("input") as f:
    f = f.read().split("\n")
    coords = [i.split(" -> ") for i in f]

rocks = set()
for rock_line in coords:
    for i in range(len(rock_line) - 1):
        x1, y1 = eval(rock_line[i])
        x2, y2 = eval(rock_line[i + 1])
        dx, dy = (x2 - x1), (y2 - y1)
        dr = (dx // abs(dx)) if dx != 0 else 0, (dy // abs(dy)) if dy != 0 else 0
        for d in range(max(abs(dx), abs(dy)) + 1):
            rocks.add((x1 + (dr[0] * d), y1 + (dr[1] * d)))


def ground_check(x, y):
    for point in list(filter(lambda p: p[0] == x, rocks)):
        if y < point[1]:
            return False
    return True


def sand_move(x, y, count):

    if ground_check(x, y):
        print(count)
        exit()

    if (x, y + 1) not in rocks:
        y += 1
        return sand_move(x, y, count)

    if (x - 1, y + 1) not in rocks or (x + 1, y + 1) not in rocks:
        if (x - 1, y + 1) not in rocks:
            x -= 1
        elif (x + 1, y + 1) not in rocks:
            x += 1
        y += 1
        return sand_move(x, y, count)

    return x, y


count = 0
while True:
    rocks.add(sand_move(500, 0, count))
    count += 1


