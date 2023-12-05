
with open("input", "r") as f:
    seed_line = f.readline()
    f.readline()
    seeds = [int(s) for s in seed_line[7:].split(" ")]
    maps = []
    mapping = []
    for i, line in enumerate(f.readlines()):
        if i == 0 or line == "\n":
            continue
        if not line[0].isnumeric():
            maps.append(mapping)
            mapping = []
            continue
        mapping.append(tuple(int(s) for s in line.split(" ")))
    maps.append(mapping)


for map in maps:
    for i in range(len(seeds)):
        for instr in map:
            dest_start = instr[0]
            source_start = instr[1]
            range_len = instr[2]
            diff = seeds[i] - source_start
            if 0 <= diff < range_len:
                seeds[i] = dest_start + diff
                break

print(min(seeds))

