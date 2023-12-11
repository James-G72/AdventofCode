
first = True
lines = []
for line in open("Day11_input.txt").read().split("\n"):
    width = len(line)
    lines.append(line)
    if all([x == "." for x in line]):
        lines.append("."*width)

pos = 0
while pos < width:
    if all([x[pos] == "." for x in lines]):
        for idx, line in enumerate(lines):
            lines[idx] = line[:pos]+"."+line[pos:]
        pos += 2
        width += 1
    else:
        pos += 1

galaxy_dixt = {}
count = 0
for row, line in enumerate(lines):
    for col, entry in enumerate(line):
        if entry == "#":
            galaxy_dixt["#"+str(count)] = [row, col]
            count += 1

distances = {}
for galaxy_1 in galaxy_dixt.keys():
    for galaxy_2 in galaxy_dixt.keys():
        if galaxy_1 != galaxy_2 and (galaxy_1+":"+galaxy_2 not in distances.keys() and galaxy_2+":"+galaxy_1 not in distances.keys()):
            loc_1 = galaxy_dixt[galaxy_1]
            loc_2 = galaxy_dixt[galaxy_2]
            height_diff = abs(loc_1[0]-loc_2[0])
            width_diff = abs(loc_1[1] - loc_2[1])
            distances[galaxy_1+":"+galaxy_2] = height_diff+width_diff

print("Part 1: Distances = "+str(sum(distances.values())))


