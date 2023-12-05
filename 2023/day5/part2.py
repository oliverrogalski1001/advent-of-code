
with open("input_test", "r") as f:
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

    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    print(seeds)

    for map in maps:
        shifted = []
        for seed_range in seeds:
            temp = [seed_range]
            for instr in map:
                next_seed_range = temp
                temp = []
                for new_seed_range in next_seed_range:
                    instr_range = (instr[1], instr[1] + instr[2])
                    shift = instr[1] - instr[0]
                    if seed_range[0] >= instr_range[0] and seed_range[1] <= instr_range[1]:
                        temp.append((seed_range[0] + shift, seed_range[1] + shift))
                    elif seed_range[0] <= instr_range[0] and seed_range[1] >= instr_range[1]:
                        temp.append((seed_range[0], instr_range[0] - 1))
                        temp.append((instr_range[0] + shift, instr_range[1] + shift))
                        temp.append((instr_range[1] + 1, seed_range[1]))
                    elif seed_range[0] < instr_range[0] and seed_range[1] <= instr_range[1]:
                        temp.append((seed_range[0], instr_range[0] - 1))
                        temp.append((instr_range[0] + shift, seed_range[1] + shift))
                    elif seed_range[0] >= instr_range[0] and seed_range[1] > instr_range[1]:
                        temp.append((seed_range[0] + shift, instr_range[1] + shift))
                        temp.append((instr_range[1] + 1, seed_range[1]))


