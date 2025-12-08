import re
import math

lines = []
actions = []
for line in open("Day6_input.txt").readlines():
    if "*" in line or "+" in line:
        actions = re.findall("\S",line.split("\n")[0])
    else:
        lines.append(re.findall("\d+", line.split("\n")[0]))

total = 0
for idx, action in enumerate(actions):
    num_list = [int(x[idx]) for x in lines]
    if action == "+":
        total += sum(num_list)
    else:
        total += math.prod(num_list)

print("Part1: The sum of invalid entries is: "+str(total))

# Part 2