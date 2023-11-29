import math
info = open("Day5_Input.txt").read().split("\n")

# --------- Part 1 ----------
stack_row = []
for x in info:
    if x[0] == " " and x[1].isdigit():
        stack_width = int(x[-1])
        break
    else:
        stack_row.append(x)
moves = info[len(stack_row)+2:]

columns = [[] for x in range(0,9)]
for stack in stack_row[::-1]:
    char_ind = 0
    while char_ind < len(stack):
        if stack[char_ind] not in [" ","[","]"]:
            columns[math.floor(char_ind/4)].append(stack[char_ind])
        char_ind += 1

for move in moves:
    move_list = move.split(" ")
    nums = [int(move_list[1]),int(move_list[3])-1,int(move_list[-1])-1]
    for pick in range(0,nums[0]):
        columns[nums[2]].append(columns[nums[1]][-1])
        columns[nums[1]] = columns[nums[1]][:-1]

p1_string = ""
for column in columns:
    if column != []:
        p1_string += column[-1]
    else:
        p1_string += " "
print("Part 1: "+p1_string)

# ---------- Part 2 -----------
columns = [[] for x in range(0,9)]
for stack in stack_row[::-1]:
    char_ind = 0
    while char_ind < len(stack):
        if stack[char_ind] not in [" ","[","]"]:
            columns[math.floor(char_ind/4)].append(stack[char_ind])
        char_ind += 1

for move in moves:
    move_list = move.split(" ")
    nums = [int(move_list[1]),int(move_list[3])-1,int(move_list[-1])-1]
    append_list = columns[nums[1]][-nums[0]:]
    for pick in append_list:
        columns[nums[2]].append(pick)
    columns[nums[1]] = columns[nums[1]][:-nums[0]]

p2_string = ""
for column in columns:
    if column != []:
        p2_string += column[-1]
    else:
        p2_string += " "
print("Part 2: "+p2_string)