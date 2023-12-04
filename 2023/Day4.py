
total = 0
for line in open("Day1_input.txt").read().split("\n"):
    winners_string, numbers_string = line.split(":")[1].split("|")
    winners_list = [x for x in winners_string.split(" ") if x != ""]
    numbers_list = [x for x in numbers_string.split(" ") if x != ""]
    counter = 0
    for num in numbers_list:
        if num in winners_list:
            counter += 1
    print(counter)
    total += (counter != 0) * (1 * 2**(counter-1))

print("Total sum is: "+str(int(total)))
