global TOTAL_CARDS

total = 0
for line in open("Day1_input.txt").read().split("\n"):
    winners_string, numbers_string = line.split(":")[1].split("|")
    winners_list = [x for x in winners_string.split(" ") if x != ""]
    numbers_list = [x for x in numbers_string.split(" ") if x != ""]
    counter = 0
    for num in numbers_list:
        if num in winners_list:
            counter += 1
    total += (counter != 0) * (1 * 2**(counter-1))

print("Total sum is: "+str(int(total)))

# Part 2
LINE_WINNERS = []
for line in open("Day1_input.txt").read().split("\n"):
    winners_string, numbers_string = line.split(":")[1].split("|")
    winners_list = [x for x in winners_string.split(" ") if x != ""]
    numbers_list = [x for x in numbers_string.split(" ") if x != ""]
    counter = 0
    for num in numbers_list:
        if num in winners_list:
            counter += 1
    LINE_WINNERS.append(counter)

TOTAL_CARDS = 0

def counting_points(card, count):
    count += 1
    global TOTAL_CARDS
    TOTAL_CARDS += 1
    if LINE_WINNERS[card] != 0:
        for x in range(0, LINE_WINNERS[card]):
            count = counting_points(card+x+1, count)
    return count

for pos in range(0, len(LINE_WINNERS)):
    counting_points(pos, 0)

print("Total sum is: "+str(int(TOTAL_CARDS)))
