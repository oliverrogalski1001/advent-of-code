
with open("input") as f:
    f = f.read().split("\n")
    coords = [i.split(" -> ") for i in f]

rocks = set()
floor = 0
for rock_line in coords:
    for i in range(len(rock_line) - 1):
        x1, y1 = eval(rock_line[i])
        x2, y2 = eval(rock_line[i + 1])
        dx, dy = (x2 - x1), (y2 - y1)
        dr = (dx // abs(dx)) if dx != 0 else 0, (dy // abs(dy)) if dy != 0 else 0
        for d in range(max(abs(dx), abs(dy)) + 1):
            rocks.add((x1 + (dr[0] * d), y1 + (dr[1] * d)))
        floor = max(y1, y2) if y1 > floor or y2 > floor else floor


def sand_move(x, y):

    if y == floor + 1:
        return x, y

    if (x, y + 1) not in rocks:
        y += 1
        return sand_move(x, y)

    if (x - 1, y + 1) not in rocks or (x + 1, y + 1) not in rocks:
        if (x - 1, y + 1) not in rocks:
            x -= 1
        elif (x + 1, y + 1) not in rocks:
            x += 1
        y += 1
        return sand_move(x, y)

    return x, y


count = 1
while True:
    new_sand = sand_move(500, 0)
    if new_sand[0] == 500 and new_sand[1] == 0:
        print(count)
        exit()
    rocks.add(new_sand)
    count += 1
