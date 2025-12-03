
batteries = [x[:-1] for x in open("Day3_input.txt").readlines()]

def max_ints(bats):
    bat_list = [int(x) for x in bats]
    jolts = ""
    search = 9
    idx = 0
    end = len(bat_list) - 1
    while search > 0 and len(jolts) < 2:
        if len(jolts) == 0:
            _bat_left = bat_list[idx:end]
        else:
            _bat_left = bat_list[idx:]
        idx_hits = [i for i, x in enumerate(_bat_left) if x == search]
        if len(idx_hits) > 0:
            jolts = jolts + str(search)
            idx = idx_hits[0] + 1
            search = 10
        search -= 1
    return jolts

total_jolts = 0
for battery in batteries:
    max_jolts = max_ints(battery)
    total_jolts += int(max_jolts)

print("Part1: The sum of invalid entries is: "+str(total_jolts))

# Part 2

def twelve_bats(bats):
    bat_list = [int(x) for x in bats]
    search = 1
    while len(bat_list) > 12:
        idx = 0
        while idx < len(bat_list):
            if bat_list[idx] == search:
                del(bat_list[idx])
                idx -= 1
            if len(bat_list) == 12:
                break
            idx += 1
        search += 1

    print(bat_list)
    return int("".join([str(x) for x in bat_list]))


total_jolts = 0
for battery in batteries:
    max_jolts = twelve_bats(battery)
    total_jolts += max_jolts

# Part 2 is incorrect as it does not consider the fact that leaving a smaller number in the sequence at the end, will make a larger number a power of 10 higher.

print("Part2: The sum of invalid entries is: "+str(total_jolts))
