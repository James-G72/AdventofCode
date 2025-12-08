import math

ranges = []
ingredients = []
gap = False
for line in open("Day5_input.txt").readlines():
    line = line.split("\n")[0]
    if gap:
        ingredients.append(int(line))
    elif line == "":
        gap = True
    else:
        ranges.append([int(x) for x in line.split("-")])

fresh = 0
for ingredient in ingredients:
    for id_range in ranges:
        if id_range[0] <= ingredient <= id_range[1]:
            fresh += 1
            break

print("Part1: The sum of invalid entries is: "+str(fresh))

# Part 2

def reduce_sets(sets):
    change = 0
    sets_out = []
    marked_indexes = []
    for idx_1, set_1 in enumerate(sets):
        if idx_1 not in marked_indexes:
            _set = set_1
            for idx_2, set_2 in enumerate(sets):
                if idx_2 > idx_1:
                    if set_1[0] <= set_2[0] <= set_1[1]:
                        _set = [min(set_1[0], set_2[0]),max(set_1[1], set_2[1])]
                        marked_indexes.append(idx_2)
                        change = 1
                        break
                    elif set_1[0] <= set_2[1] <= set_1[1]:
                        _set = [min(set_1[0], set_2[0]),max(set_1[1], set_2[1])]
                        marked_indexes.append(idx_2)
                        change = 1
                        break
            sets_out.append(_set)

    return change, sets_out


reduced = 1
while reduced:
    reduced, ranges = reduce_sets(ranges)
    print(f"Remaining: {len(ranges)}")

fresh = 0
for id_range in ranges:
    span = id_range[1]-id_range[0] + 1
    fresh += span

print("Part2: The sum of invalid entries is: "+str(fresh))