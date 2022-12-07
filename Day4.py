pairs = open("Day4_Input.txt").read().split("\n")

# ------- Part 1 ---------
p1_count = 0
for pair in pairs:
    elves = pair.split(",")
    if int(elves[0].split("-")[0]) < int(elves[1].split("-")[0]):
        if int(elves[0].split("-")[-1]) >= int(elves[1].split("-")[-1]):
            p1_count += 1
    elif int(elves[0].split("-")[0]) > int(elves[1].split("-")[0]):
        if int(elves[0].split("-")[-1]) <= int(elves[1].split("-")[-1]):
            p1_count += 1
    else:
        p1_count += 1

print("Part 1: "+str(p1_count))