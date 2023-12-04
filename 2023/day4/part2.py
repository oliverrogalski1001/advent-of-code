
cards = []
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        a, b = line.split("|")
        a = a[a.find(":") + 2:]
        win_nums = [num for num in a.split(" ") if num != ""]
        card_nums = [num for num in b.split(" ") if num != ""]
        win_num_set = {int(win_num) for win_num in win_nums}
        card_nums_list = [int(card_num) for card_num in card_nums]
        cards.append((win_num_set, card_nums_list))

counts = [1] * len(cards)
for i, (win_set, nums) in enumerate(cards):
    score = 0
    for num in nums:
        if num in win_set:
            score += 1
    for j in range(1, score + 1):
        counts[i + j] += counts[i]

print(sum(counts))
