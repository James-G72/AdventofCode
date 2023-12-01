list_sum = 0
for line in open("Day1_input.txt").read().split("\n"):
    flip_line = line[::-1]
    first = False
    last = False
    iter = 0
    value = [0,0]
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


# Part 2

def check_words(place,full,flip=False):
    """
    Checks for a number spelt out in words. If found will return True and the number.
    :param full: str, full line
    :param flip: bool, tells the function whether or not to flip the word
    :return: check (bool for if the check found a word), result (int of result)
    """
    word3, word4, word5 = "0", "0", "0"
    if not flip:
        if place+3 <= len(full):
            word3 = full[place:place+3]
        if place+4 <= len(full):
            word4 = full[place:place+4]
        if place+5 <= len(full):
            word5 = full[place:place+5]
    else:
        if place >= 2:
            word3 = full[len(full)-(place+1):len(full)-(place+1)+3]
        if place >= 3:
            word4 = full[len(full)-(place+1):len(full)-(place+1)+4]
        if place >= 4:
            word5 = full[len(full)-(place+1):len(full)-(place+1)+5]
    if word3.isalpha():
        if word3 == "one":
            return True,1
        elif word3 == "two":
            return True,2
        elif word3 == "six":
            return True,6
    if word4.isalpha():
        if word4 == "four":
            return True,4
        if word4 == "five":
            return True,5
        if word4 == "nine":
            return True,9
    if word5.isalpha():
        if word5 == "three":
            return True,3
        if word5 == "seven":
            return True,7
        if word5 == "eight":
            return True,8
    return False, 0


list_sum = 0
words = ["one","two","three","four","five","six","seven","eight","nine"]
STARTS = set([x[0] for x in words])
digits = [1,2,3,4,5,6,7,8,9]
NUM_DICT = dict(zip(digits,words))

for line in open("Day1_input.txt").read().split("\n"):
    flip_line = line[::-1]
    first = False
    last = False
    iter = 0
    value = [0,0]
    limit = len(line)
    while not first or not last:
        f = line[iter]
        l = flip_line[iter]
        if f.isdigit() and not first:
            first = True
            value[0] = int(f)
        elif f in STARTS and not first:
            first, value[0] = check_words(iter,line,False)
        if l.isdigit() and not last:
            last = True
            value[1] = int(l)
        elif l in STARTS and not last:
            last, value[1] = check_words(iter,line,True)
        iter += 1
        print(value)
    list_sum += int(str(value[0])+str(value[1]))

print("The sum of all calibration values is: "+str(list_sum))
