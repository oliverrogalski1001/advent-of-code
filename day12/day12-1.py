from collections import deque

with open("input") as f:
    f = f.read().split("\n")
    f = [list(i) for i in f]
    for i in range(len(f)):
        f[i] = [ord(i) - 97 for i in f[i]]
    sr = sc = er = ec = 0
    for i, arr in enumerate(f):
        for j, val in enumerate(arr):
            if val == -14:
                f[i][j] = 0
                sr, sc = i, j
            if val == -28:
                f[i][j] = 25
                er, ec = i, j
    visited = {(0, 0)}


q = deque()
q.append((sr, sc, 0))
while len(q) > 0:
    r, c, count = q.popleft()
    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in di:
        newR = r + d[0]
        newC = c + d[1]
        if newR >= len(f) or newC >= len(f[0]) or newR < 0 or newC < 0:
            continue
        if (newR, newC) in visited or f[newR][newC] - f[r][c] > 1:
            continue
        if r == er and c == ec:
            print(count)
            exit()
        visited.add((newR, newC))
        q.append((newR, newC, count + 1))
