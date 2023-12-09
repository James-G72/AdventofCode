
# pos = False
# map_dict = {}
# for line in open("Day8_input.txt").read().split("\n"):
#     if not pos:
#         instructs = line
#         pos = True
#     elif line != "":
#         map_dict[line.split("=")[0].replace(" ","")] = line.split("=")[1].replace(" ","").replace("(","").replace(")","").split(",")
#
# t = 1
# found = False
# pos = 0
# reset_track = 0
# options = "LR"
# map = "AAA"
# while not found:
#     if pos > len(instructs)-1:
#         reset_track += pos
#         pos = 0
#     map = map_dict[map][options.index(instructs[pos])]
#     pos += 1
#     if pos == 280:
#         t = 1
#     if map == "ZZZ":
#         print("Found!")
#         found = True
# reset_track += pos
#
# print("Part 1: "+str(reset_track))

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

def detect_patern(map_, map_dict, inst):
    tracker = {}
    options = "LR"
    pos = 0
    reset_track = 0
    tracker[map_+str(pos)] = 0
    z_s = []
    while True:
        if pos > len(instructs)-1:
            reset_track += pos
            pos = 0
        map_ = map_dict[map_][options.index(inst[pos])]
        if map_[-1] == "Z":
            z_s.append([reset_track+pos])
        pos += 1
        if map_+str(pos) in tracker.keys():
            return reset_track+pos, tracker[map_+str(pos)], z_s
        else:
            tracker[map_+str(pos)] = reset_track+pos

loop_info = [0]*len(start_keys)
for idx, key in enumerate(start_keys):
    loop_info[idx] = detect_patern(key, map_dict, instructs)

answer = 0
counter_list = [x[2][0][0] for x in loop_info]
steps = [int((loop_info[x][0]-loop_info[x][1])/len(loop_info[x][2])) for x in range(0, len(loop_info))]
found = False
while not found:
    if all([x == counter_list[0] for x in counter_list]):
        answer = counter_list[0]
        found = True
    else:
        idx = counter_list.index(min(counter_list))
        counter_list[idx] += steps[idx]
    t = 1


print("Part 2: "+str(answer+1))