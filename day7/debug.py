from collections import Counter

card_order = '23456789TJQKA'
card_order2 = 'J23456789TQKA'

def hand_value(hand, j=False):
    if j:
        counts = Counter(hand)
        j_count = counts['J']
        counts.subtract({'J': j_count})
        counts.update({counts.most_common(1)[0][0]: j_count})
        freqs = Counter(counts.values())
    else:
        freqs = Counter(Counter(hand).values())
    if 5 in freqs:
        return 5
    if 4 in freqs:
        return 4
    if 3 in freqs:
        if 2 in freqs:
            return 3.5
        return 3
    if 2 in freqs:
        if freqs[2] == 2:
            return 2
        return 1
    return 0

f = open('input.txt', 'r')
poker_list = list(map(lambda x: tuple(x.split()), f.read().strip().split('\n')))
# Part 1
sorted_list = sorted(poker_list, key=lambda x: (hand_value(x[0]), [card_order.index(c) for c in x[0]]))
p1 = sum(int(val[-1]) * (idx + 1) for idx, val in enumerate(sorted_list))
print(p1)
# Part 2
sorted_list = sorted(poker_list, key=lambda x: (hand_value(x[0], j=True), [card_order2.index(c) for c in x[0]]))
p2 = sum(int(val[-1]) * (idx + 1) for idx, val in enumerate(sorted_list))
print(p2)