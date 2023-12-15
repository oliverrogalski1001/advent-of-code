
with open("input", "r") as f:
    seq = f.readline().split(",")

def hash_func(chars):
    curr_hash = 0
    for c in chars:
        curr_hash = ((curr_hash + ord(c)) * 17) % 256
    return curr_hash

hashmap = [[] for _ in range(256)]
for s in seq:
    equals = "=" in s
    label, focal = s.split("=" if equals else "-")
    if focal != "":
        focal = int(focal)
    hashed = hash_func(label)
    box = hashmap[hashed]
    if equals:
        found = False
        for i, lens in enumerate(box):
            if lens[0] == label:
                box[i] = (label, focal)
                found = True
                break
        if not found:
            box.append((label, focal))
    else:
        del_i = -1
        for i, lens in enumerate(box):
            if lens[0] == label:
                del_i = i
        if del_i >= 0:
            box.pop(del_i)

hash_sum = 0
for i, box in enumerate(hashmap):
    for j, lens in enumerate(box):
        hash_sum += (i + 1) * (j + 1) * lens[1]

print(hash_sum)
