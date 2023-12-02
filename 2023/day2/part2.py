
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

power_sum = 0
for game in games:
    bag = games[game]
    color_mins = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for tup in bag:
        color_mins[tup[0]] = max(color_mins.get(tup[0]), tup[1])
    power_sum += color_mins["red"] * color_mins["green"] * color_mins["blue"]

print(power_sum)
