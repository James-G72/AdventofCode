
def hand_type(cards):
    """
    A function that iterates through the hand in order to establish which type of hand it is
    :param hand: str, input of the hand to be considered
    :return:
    """
    counts = {}
    for card in cards:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(), reverse=True)

def type_to_score(cards):
    # Attempting to create a universal score
    card_order = "23456789TJQKA"
    mid = hand_type(cards)
    mid.extend([card_order.index(x) for x in cards])
    return mid

scores = []
for line in open("Day7_input.txt").read().split('\n'):
    cards, bid = line.split()
    score = type_to_score(cards)
    scores.append([score, cards, int(bid)])
# Essentially sorting by the length of the score
scores.sort()

total = 0
for idx, hand_info in enumerate(scores):
    bid = hand_info[2]
    total += (idx+1) * bid

print("Part 1: "+str(total))

# Part 2
def hand_type(cards):
    """
    A function that iterates through the hand in order to establish which type of hand it is
    :param hand: str, input of the hand to be considered
    :return:
    """
    counts = {}
    for card in cards:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(),reverse=True)

def type_to_score(cards):
    # Attempting to create a universal score
    card_order = "23456789TJQKA"
    mid = hand_type(cards)
    mid.extend([card_order.index(x) for x in cards])
    return mid

def handling_jokers(cards):
    """
    Key is that there are 2 cases, either all jokers, in which case change to all aces, or change joker to the highest card you have the most of
    :param cards: str, hand to be changed
    :return: str, new_hand
    """
    card_order = "23456789TQKA"
    if cards == "JJJJJ":
        cards = "AAAAA"
    else:
        rank_count = [0] * len(card_order)
        for card in cards:
            if card != "J":
                rank_count[card_order.index(card)] += 1
        if sum(rank_count) == 3:
            t = 1
        if max(rank_count) >= 3:
            replace_card = card_order[rank_count.index(max(rank_count))]
        else:
            replace_card = card_order[max([idx for idx,x in enumerate(rank_count) if x == (max(rank_count))])]
        cards = cards.replace("J",replace_card)

    return cards


scores = []
for line in open("Day7_input.txt").read().split('\n'):
    cards, bid = line.split()
    cards = handling_jokers(cards)
    score = type_to_score(cards)
    scores.append([score, cards, int(bid)])
# Essentially sorting by the length of the score
scores.sort()

total = 0
for idx,hand_info in enumerate(scores):
    bid = hand_info[2]
    total += (idx+1) * bid

print("Part 2: "+str(total))