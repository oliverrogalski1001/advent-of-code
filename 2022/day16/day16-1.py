
with open("input") as f:
    f = f.read().split("\n")

g = {}
flow = {}
indexes = {}
count = 0
zeros = 0
for line in f:
    s = line.split(" ")
    valve = s[1]

    rate = line.split("=")[1]
    rate = int(rate[:rate.index(";")])

    c = s[9:]
    for i in range(len(c) - 1):
        c[i] = c[i][:-1]

    g[valve] = c
    flow[valve] = rate
    indexes[valve] = count
    count += 1
    if rate == 0:
        zeros += 1

print(g)
print(flow)

warshall = [[100] * len(g) for _ in range(len(g))]
for i in range(len(g)):
    warshall[i][i] = 0

for node in g.keys():
    for tunnel in g[node]:
        warshall[indexes[node]][indexes[tunnel]] = 1
        warshall[indexes[tunnel]][indexes[node]] = 1

for k in range(len(g)):
    for i in range(len(g)):
        for j in range(len(g)):
            if warshall[i][j] > warshall[i][k] + warshall[k][j]:
                warshall[i][j] = warshall[i][k] + warshall[k][j]

print(warshall)
visited = set()
def dp(curr_node, visited, time):
    if time <= 0 or len(visited) == (len(g) - zeros):
        return 0
    if curr_node != "AA":
        visited.add(curr_node)
    step = []
    for next_node in g.keys():
        if next_node not in visited and flow[next_node] != 0:
            step_flow = dp(next_node, visited.copy(), time - warshall[indexes[curr_node]][indexes[next_node]] - 1)
            step.append(step_flow)
    if len(step) == 0:
        return flow[curr_node] * time
    return (flow[curr_node] * time) + max(step)

print(dp("AA", visited, 30))
# for node in g.keys():
#     if node == "aa":
#         continue
#     if flow[node] == 0:
#         zeros.append(node)
#         for tunnel in g[node]:

# mem = {}
# on_valves = {node : False for node in g.keys()}
# def dp(curr_node, on, time):
#     if time <= 1:
#         return 0
#     if flow[curr_node] == 0 or on[curr_node]:
#         return max(dp(b, on, time - 1) for b in g[curr_node])
#     if not on[curr_node]:
#         new_on = on.copy()
#         new_on[curr_node] = True
#         return (flow[curr_node] * (time - 1)) + max(dp(b, new_on, time - 2) for b in g[curr_node])

