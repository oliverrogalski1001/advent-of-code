
lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

games = {}
for line in lines:
    num = int(line[5:line.index(":")])
    bags = line[line.index(":") + 2:].split(";")
    dict_list = []
    for bag in bags:
        items = bag.strip().split(",")
        for item in items:
            item = item.strip()
            num_item = int(item[:item.find(" ")])
            color = item[item.find(" ") + 1:]
            dict_list.append((color, num_item))
    games[num] = dict_list

limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}
sum_games = 0
for game in games:
    possible = True
    for color, num in games[game]:
        if num > limit[color]:
            possible = False
            break
    if possible:
        sum_games += game

print(sum_games)
