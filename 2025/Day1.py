
input_list = []
for line in open("Day1_input.txt").read().split("\n"):
    input_list.append(line)

pos = 50
counter = 0
for x in input_list:
    dif = int(x[1:])
    if dif >= 99:
        rot, dif = divmod(dif, 100)
    if x[0] == "L":
        pos -= dif
        if pos < 0:
            pos = pos % 100
    else:
        pos += dif
        if pos > 99:
            pos = pos % 100
    if pos == 0:
        counter += 1

print("Part1: The total number of 0's is: "+str(counter))

# Part 2
input_list = []
for line in open("Day1_input.txt").read().split("\n"):
    input_list.append(line)

instructions = [(-1 if line[0] == 'L' else 1) * int(line[1:]) for line in input_list]

counter = 0
current = 50
for steps in instructions:
    start = current
    # Count carries
    counter += int(abs(steps) / 100)
    # Add remainder and mod
    current = (current + steps) % 100
    # Check if the start value and current value are both no-zero
    if start != 0 and current != 0:
        # Check if we've wrapped either way
        if (steps < 0 and current > start) or (steps > 0 and current < start):
            counter += 1
    if current == 0:
        counter += 1

print("Part2: The total number of 0's passed: "+str(counter))
