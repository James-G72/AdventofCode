
total = 0
for line in open("Day4_input.txt").read().split("\n"):
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
for line in open("Day4_input.txt").read().split("\n"):
    winners_string, numbers_string = line.split(":")[1].split("|")
    winners_list = [x for x in winners_string.split(" ") if x != ""]
    numbers_list = [x for x in numbers_string.split(" ") if x != ""]
    counter = 0
    for num in numbers_list:
        if num in winners_list:
            counter += 1
    LINE_WINNERS.append(counter)

def counting_points(card, count):
    count += 1
    if LINE_WINNERS[card] != 0:
        for x in range(0, LINE_WINNERS[card]):
            count = counting_points(card+x+1, count)
    return count

card_num = 0
for pos in range(0, len(LINE_WINNERS)):
    card_num += counting_points(pos, 0)

print("Total number of cards is: "+str(int(card_num)))
