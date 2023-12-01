
lines = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

nums = []
for line in lines:
    curr_num = ""
    for c in line:
        if c.isnumeric():
            curr_num += c
    curr_num = curr_num[0] + curr_num[-1]
    nums.append(int(curr_num))

print(sum(nums))

