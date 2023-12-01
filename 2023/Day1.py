list_sum = 0
for line in open("Day1_input.txt").read().split("\n"):
    flip_line = line[::-1]
    first = False
    last = False
    iter = 0
    value = [0, 0]
    if line == "zfxbzhczcx9eightwockk":
        t = 1
    while not first or not last:
        if line[iter].isdigit() and not first:
            first = True
            value[0] = int(line[iter])
        if flip_line[iter].isdigit() and not last:
            last = True
            value[1] = int(flip_line[iter])
        iter += 1
        print(value)
    list_sum += int(str(value[0])+str(value[1]))

print("The sum of all calibration values is: "+str(list_sum))