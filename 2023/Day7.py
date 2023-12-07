
def hand_type(hand):
    """
    A function that iterates through the hand in order to establish which type of hand it is
    :param hand: str, input of the hand to be considered
    :return:
    """
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(), reverse=True)

def type_to_score(hand):
    # Attempting to create a universal score
    card_order = "23456789TJQKA"
    mid = hand_type(hand)
    mid.extend([card_order.index(x) for x in hand])
    return mid

scores = []
for line in open("Day7_input.txt").read().split('\n'):
    hand, bid = line.split()
    score = type_to_score(hand)
    scores.append([score, hand, int(bid)])
# Essentially sorting by the length of the score
scores.sort()

total = 0
for idx, hand_info in enumerate(scores):
    bid = hand_info[2]
    total += (idx+1) * bid

print("Part 1: "+str(total))