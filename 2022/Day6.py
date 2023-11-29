stream = open("Day6_Input.txt").read()

# ------- Part 1 ---------
for char_ind in range(4, len(stream)):
    if len(set(stream[char_ind-4:char_ind])) == 4:
        print("Part 1: "+str(char_ind))
        break

# -------- Part 2 ---------
for char_ind in range(14, len(stream)):
    if len(set(stream[char_ind-14:char_ind])) == 14:
        print("Part 2: "+str(char_ind))
        break