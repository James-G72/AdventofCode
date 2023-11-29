rucksacks = open("Day3_Input.txt").read().split("\n")

# ----------  Part 1  ------------
p1_score = 0
for sack in rucksacks:
    split_point = int(len(sack)/2)
    for x in sack[:split_point]:
        if x in sack[split_point:]:
            if x == x.lower():
                p1_score += ord(x)-96
            else:
                p1_score += ord(x)-38
            break

print("Part 1: "+str(p1_score))

# ---------- Part 2  ------------
p2_score = 0
for group in range(0, int(len(rucksacks)/3)):
    elf_1 = rucksacks[group*3]
    elf_2 = rucksacks[group*3+1]
    elf_3 = rucksacks[group*3+2]
    for x in elf_1:
        if x in elf_2:
            if x in elf_3:
                if x == x.lower():
                    p2_score += ord(x)-96
                else:
                    p2_score += ord(x)-38
                break

print("Part 2: "+str(p2_score))