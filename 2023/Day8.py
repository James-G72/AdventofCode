
pos = False
map_dict = {}
for line in open("Day8_input.txt").read().split("\n"):
    if not pos:
        instructs = line
        pos = True
    elif line != "":
        map_dict[line.split("=")[0].replace(" ","")] = line.split("=")[1].replace(" ","").replace("(","").replace(")","").split(",")

t = 1
found = False
pos = 0
reset_track = 0
options = "LR"
map = "AAA"
while not found:
    if pos > len(instructs)-1:
        reset_track += pos
        pos = 0
    map = map_dict[map][options.index(instructs[pos])]
    pos += 1
    if pos == 280:
        t = 1
    if map == "ZZZ":
        print("Found!")
        found = True
reset_track += pos

print("Part 1: "+str(reset_track))

# Part 2

pos = False
map_dict = {}
for line in open("Day8_input.txt").read().split("\n"):
    if not pos:
        instructs = line
        pos = True
    elif line != "":
        map_dict[line.split("=")[0].replace(" ","")] = line.split("=")[1].replace(" ","").replace("(","").replace(")","").split(",")

start_keys = []
for key in map_dict.keys():
    if key[-1] == "A":
        start_keys.append(key)

t = 1
found = False
pos = 0
reset_track = 0
options = "LR"
while not found:
    if pos > len(instructs)-1:
        reset_track += pos
        pos = 0
    for idx, map in enumerate(start_keys):
        start_keys[idx] = map_dict[map][options.index(instructs[pos])]
    pos += 1
    found = all([map[-1] == "Z" for map in start_keys])
reset_track += pos

print("Part 2: "+str(reset_track))