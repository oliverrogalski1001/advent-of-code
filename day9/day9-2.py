import math

with open("input") as f:
    f = f.read().split("\n")

u = {(0, 0)}
snek = [(0, 0) for i in range(10)]


def tail_move(tail, head):
    moveX = head[0] - tail[0]
    moveY = head[1] - tail[1]
    if abs(moveX) <= 1 and abs(moveY) <= 1:
        return tail
    if abs(moveX) == 2:
        moveX -= int(math.copysign(1, moveX))
    if abs(moveY) == 2:
        moveY -= int(math.copysign(1, moveY))
    return tail[0] + moveX, tail[1] + moveY


moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
for i in f:
    di, move = i.split(" ")
    for _ in range(int(move)):
        snek[0] = (snek[0][0] + moves[di][0], snek[0][1] + moves[di][1])
        for knot in range(1, len(snek)):
            snek[knot] = tail_move(snek[knot], snek[knot - 1])
        u.add(snek[-1])

print(len(u))
