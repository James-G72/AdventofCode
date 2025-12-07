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

fresh = 0
for id_range in ranges:
    span = id_range[1]-id_range[0] + 1
    fresh += span

print("Part2: The sum of invalid entries is: "+str(fresh))
