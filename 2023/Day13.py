
all_rows = []
rows = []
for line in open("Day13_input.txt").read().split("\n"):
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

def return_mirror(iter):
    truths = []
    for i, it in enumerate(iter):
        truth = []
        for x in range(0, len(it)-1):
            start = max(0,x-len(it)/2)
            end = min(len(it),x+x)
            truth.append(it[start:x] == reversed(it[x:end]))
        truths.append(truth)
    for check in range(0, len(truth)):
        if all([x[check] for x in truths]):
            return check

for pattern in patterns:
    col_idx = return_mirror(pattern[0])
    row_idx = return_mirror(pattern[1])
    t = 1