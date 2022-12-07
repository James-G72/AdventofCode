stream = open("Day6_Input.txt").read()

for char_ind in range(4, len(stream)):
    if len(set(stream[char_ind-4:char_ind])) == 4:
        print("Part 1: "+str(char_ind))