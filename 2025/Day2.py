import re

db_ranges = []
for line in open("Day2_input.txt").read().split(","):
    db_ranges.append([int(x) for x in line.split('-')])

group_pattern = r'(.+)(\1{1,})'

def check_invalid_simple(num):
    check = str(num)
    if len(check) % 2:
        return 0
    elif check[0:int(len(check)/2)] == check[int(len(check)/2):]:
        print(f"Invalid string {num}")
        return 1
    return 0

counter = 0
for db_range in db_ranges:
    for num in range(db_range[0], db_range[1]+1):
        counter += check_invalid_simple(num) * num

print("Part1: The sum of invalid entries is: "+str(counter))

# Part 2
