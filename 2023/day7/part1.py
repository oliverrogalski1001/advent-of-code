from functools import cmp_to_key

bid_map = {}
hands = []
cards = [str(i) for i in range(1, 10)] + ["T", "J", "Q", "K", "A"]
strength = {cards[i]: i for i in range(len(cards))}
with open("input", "r") as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        bid_map[hand] = int(bid)
        hands.append(hand)

def rank(hand: str):
    counts = {c: 0 for c in cards}
    for c in hand:
        counts[c] += 1
    inverse = {c: [] for c in range(1, 6)}
    for c in counts:
        if counts[c] != 0:
            inverse[counts[c]].append(c)

    if len(inverse[5]) == 1:
        return 6
    if len(inverse[4]) == 1:
        return 5
    if len(inverse[3]) == 1 and len(inverse[2]) == 1:
        return 4
    if len(inverse[3]) == 1:
        return 3
    if len(inverse[2]) == 2:
        return 2
    if len(inverse[2]) == 1:
        return 1
    return 0

def compare(hand1, hand2):
    for c1, c2 in zip(hand1, hand2):
        if strength[c1] > strength[c2]:
            return 1
        if strength[c2] > strength[c1]:
            return -1
    return 0


hand_ranks = {c: [] for c in range(0, 7)}
for hand in hands:
    hand_ranks[rank(hand)].append(hand)

count = 1
card_sum = 0
for rank in hand_ranks:
    for hand in sorted(hand_ranks[rank], key=cmp_to_key(compare)):
        card_sum += count * bid_map[hand]
        count += 1

print(card_sum)
