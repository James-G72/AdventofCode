
times = []
records = []
pos = 0
for line in open("Day6_input.txt").read().split("\n"):
    if pos == 0:
        [times.append(int(x)) for x in line.split(":")[1].split(" ") if x != ""]
        pos = 1
    else:
        [records.append(int(x)) for x in line.split(":")[1].split(" ") if x != ""]

races = 1
for idx, time in enumerate(times):
    races *= sum([(x*(time-x) > records[idx]) for x in range(0, time)])
print("Part 1 product of races is: "+str(races))

# Part 2
