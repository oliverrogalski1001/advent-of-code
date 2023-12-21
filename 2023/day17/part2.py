from math import inf
from heapq import heappush, heappop

def in_bounds(coords, height, length):
    return 0 <= coords[0] < height and 0 <= coords[1] < length

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    h = len(lines)
    l = len(lines[0])

v = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        curr_node = (i, j)
        v[curr_node] = inf

def tadd(a, b):
    return a[0] + b[0], a[1] + b[1]

def tmul(a, b):
    return a[0] * b, a[1] * b

start_cost = int(lines[0][0])
v[(0, 0)] = start_cost
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
pq = [(0, (0, 0, (0, 1), 0)), (0, (0, 0, (1, 0), 0))]
target = (h - 1, l - 1)
visited = set()

while len(pq):
    curr_node = heappop(pq)
    curr_cost = curr_node[0]
    curr_node = curr_node[1]
    if curr_node in visited:
        continue
    visited.add(curr_node)
    curr_coords = curr_node[:2]
    if curr_coords == target:
        break
    for d in dirs:
        if d == curr_node[2] and curr_node[3] >= 4:
            next_coord = tadd(curr_coords, d)
            move = 1
        else:
            next_coord = tadd(curr_coords, tmul(d, 4))
            move = 4
        if not in_bounds(next_coord, h, l) or tmul(d, -1) == curr_node[2]:
            continue
        if move == 4:
           cost = 0
           curr_c_temp = curr_coords
           for _ in range(4):
               curr_c_temp = tadd(curr_c_temp, d)
               cost += int(lines[curr_c_temp[0]][curr_c_temp[1]])
        else:
            cost = int(lines[next_coord[0]][next_coord[1]])

        if curr_cost + cost < v[next_coord]:
            if d == curr_node[2]:
                if curr_node[3] < 10:
                    v[next_coord] = curr_cost + cost
            else:
                v[next_coord] = curr_cost + cost
        if curr_node[2] == d:
            if curr_node[3] < 10:
                next_state = (curr_cost + cost, (next_coord[0], next_coord[1], d, curr_node[3] + move))
                if next_state not in visited:
                    heappush(pq, next_state)
        else:
            next_state = (curr_cost + cost, (next_coord[0], next_coord[1], d, move))
            if next_state not in visited:
                heappush(pq, next_state)

print(v[target])
