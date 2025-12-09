import math

red_locs = []
for line in open("Day9_input.txt").readlines():
    red_locs.append([int(x) for x in line.split("\n")[0].split(",")])


def rec_size(loc1, loc2):
    return (abs(loc1[0] - loc2[0]) + 1) * (abs(loc1[1] - loc2[1]) + 1)


biggest_rect = 0
for idx_1, red_loc_1 in enumerate(red_locs):
    for idx_2, red_loc_2 in enumerate(red_locs):
        if idx_1 != idx_2:
            if rec_size(red_loc_1, red_loc_2) > biggest_rect:
                biggest_rect = rec_size(red_loc_1, red_loc_2)


print("Part1: The biggest rectangle: " + str(biggest_rect))

# Part 2
