
with open("input") as f:
    f = f.read().split("\n")

u = {(0, 0)}
h = (0, 0)
h1 = (0, 0)
t = (0, 0)


def tail_move(tail, head, last_head):
    moveX = head[0] - tail[0]
    moveY = head[1] - tail[1]
    if abs(moveX) <= 1 and abs(moveY) <= 1:
        return tail
    return last_head


for i in f:
    di, move = i.split(" ")
    move = int(move)
    for _ in range(move):
        h1 = tuple(h)
        if di == "R":
            h = (h[0] + 1, h[1])
        elif di == "L":
            h = (h[0] - 1, h[1])
        elif di == "U":
            h = (h[0], h[1] + 1)
        else:
            h = (h[0], h[1] - 1)
        t = tail_move(t, h, h1)
        u.add(t)

print(len(u))
