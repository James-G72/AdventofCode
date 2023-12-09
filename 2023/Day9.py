import numpy as np

sequences = []
for line in open("Day9_input.txt").read().split("\n"):
    sequences.append([int(x) for x in line.split(" ")])

def assess_difference(line):
    gaps = np.diff(line, n=1)
    current_gap = gaps[-1]
    if not all([x == 0 for x in gaps]):
        end_list = assess_difference(gaps)
        end_list += current_gap
    else:
        return 0
    return end_list


sums = 0
for sequence in sequences:
    ends = assess_difference(sequence)
    last_number = sequence[-1] + ends
    sums += last_number

print("Part 1: "+str(sums))

# Part 2
sums = 0
for sequence in sequences:
    ends = assess_difference(sequence[::-1])
    last_number = sequence[0] + ends
    sums += last_number

print("Part 2: "+str(sums))