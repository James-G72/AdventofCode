
carry = 0
for line in open("Day15_input.txt").read().split("\n"):
    for cmd in line.split(","):
        start = 0
        for char in cmd:
            start += ord(char)
            start *= 17
            start = start % 256
        carry += start

print("Part 1: {}".format(carry))