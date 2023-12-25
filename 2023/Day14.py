
all_rows = []
rows = []
for line in open("Day14_input.txt").read().split("\n"):
    if line == "":
        all_rows.append(rows)
        rows = []
    else:
        rows.append(line)
all_rows.append(rows)

columns = []
patterns = []
col = ""
for idx,row in enumerate(all_rows):
    for pos in range(0,len(row[0])):
        for height in range(0,len(row)):
            col += row[height][pos]
        columns.append(col)
        col = ""
    patterns.append([row, columns])
    columns = []

load = 0
for pattern in patterns:
    cols = pattern[1]
    for col in cols:
        base = len(col)
        for idx, place in enumerate(col):
            if place == "O":
                load += base
                base -= 1
            elif place == "#":
                base = len(col) - idx - 1

print("Part 1: {}".format(load))