import pandas as pd

hands = []
bids = []
for line in open("Day7_input.txt").read().split("\n"):
    h, b = line.split(" ")
    hands.append([char for char in h])
    bids.append(b)

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
order = [13-x for x in range(0, 14)]
rank_dict = dict(zip(cards, order))

strength = []
strength = pd.Series()
for idx, hand in enumerate(hands):
    rank_count = [0]*14
    for card in hand:
        rank_count[rank_dict[card]] += 1
    if max(rank_count) == 5:
        strength._set_value(1000000000+rank_dict[hand[0]], "".join(hand))
    elif max(rank_count) == 4:
        main_card = [idx for idx, r in enumerate(rank_count) if r == max(rank_count)][0]
        other_card = [rank_dict[c] for idx, c in enumerate(hand) if rank_dict[c] != main_card][0]
        base = 1+main_card
        possitional = [idx for idx, c in enumerate(hand) if rank_dict[c] != main_card][0]
        stren = 100000000 + possitional*13 + other_card
        strength._set_value(stren, "".join(hand))
    # elif max(rank_count) == 3:
    #
    # elif max(rank_count) == 2:
    #
    # elif max(rank_count) == 1:

print(strength.sort_index(ascending=False))