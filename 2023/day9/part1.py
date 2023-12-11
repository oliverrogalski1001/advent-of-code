
with open("input", "r") as f:
    seqs = [[int(x.strip()) for x in line.split(" ")] for line in f.readlines()]

def seq_diff(arr):
    return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]

sums = 0
for seq in seqs:
    diffs = [seq]
    temp = seq

    while temp.count(temp[0]) != len(temp):
        temp_diff = seq_diff(temp)
        temp = temp_diff
        diffs.append(temp)

    curr_num = diffs[-1][-1]
    for diff in reversed(diffs[:-1]):
        curr_num += diff[-1]

    sums += curr_num

print(sums)
