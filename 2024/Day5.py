import itertools



orders = []
pages = []
space = False
for line in open("Day5_input.txt").read().split("\n"):
    if line == "":
        space = True
    else:
        if not space:
            orders.append([int(line.split("|")[0]), int(line.split("|")[1])])
        else:
            pages.append([int(x) for x in line.split(",")])

total = 0

def return_valid(first, last, page_list):
    for page in page_list:
        if page == first:
            return True
        elif page == last and first in page_list:
            return False
    if first not in page_list or last not in page_list:
        return True
    return False

def isvalid_update(page_list, orders):
    correct = []
    for order in orders:
        first = order[0]
        last = order[1]
        correct.append(return_valid(first, last, page_list))
    if all(correct):
        return True

def make_valid(page_list, orders):
    possible_lists = list(itertools.permutations(page_list))
    print(len(possible_lists))
    for possible_list in possible_lists:
        if isvalid_update(possible_list, orders):
            return possible_list

total = 0
for idx, page_list in enumerate(pages):
    if isvalid_update(page_list, orders):
        total += page_list[int((len(page_list)-1) / 2)]

print("Lowest location is: "+str(total))

# Part 2

total = 0
for idx, page_list in enumerate(pages):
    if isvalid_update(page_list, orders):
        pass
    else:
        valid_order = make_valid(page_list, orders)
        total += valid_order[int((len(page_list)-1) / 2)]
    print("Done")

print(total)