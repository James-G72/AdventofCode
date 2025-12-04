
batteries = [x[:-1] for x in open("Day3_input.txt").readlines()]

def biggest_bats_general(bats, bat_num):
    """
    Trying to generalise for battery choices of any length.
    Intentionally direct for readability
    :param bats: String representing the batteries available
    :param bat_num: Number of batteries to choose
    :return:
    """
    if bats == "818181911112111":
        t = 1
    bat_list = [int(x) for x in bats]
    jolts = ""
    start = 0
    while len(jolts) < bat_num:
        search = 9
        end = len(bat_list) - (bat_num - 1 - len(jolts))
        cont = True
        while search > 0 and cont == True:
            for idx, num in enumerate(bat_list[start:end]):
                if num == search:
                    start = start + idx + 1
                    jolts = jolts + str(search)
                    cont = False
                    break
            search -= 1

    return jolts


total_jolts = 0
for battery in batteries:
    max_jolts = biggest_bats_general(battery, 2)
    total_jolts += int(max_jolts)

print("Part1: The sum of invalid entries is: "+str(total_jolts))

# Part 2

total_jolts = 0
for battery in batteries:
    max_jolts = biggest_bats_general(battery, 12)
    print(max_jolts)
    total_jolts += int(max_jolts)

# Part 2

print("Part2: The sum of invalid entries is: "+str(total_jolts))
