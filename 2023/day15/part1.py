
with open("input", "r") as f:
    seq = f.readline().split(",")

hash_sum = 0
for s in seq:
    curr_hash = 0
    for c in s:
        curr_hash += ord(c)
        curr_hash = (curr_hash * 17) % 256
    hash_sum += curr_hash

print(hash_sum)
