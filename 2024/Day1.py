list_sum = 0
list1 = []
list2 = []
for line in open("Day1_input.txt").read().split("\n"):
    a, b = line.split("  ")
    list1.append(int(a))
    list2.append(int(b))

index_list = [x for x in range(0, len(list1))]

list1_comp = zip(list1, index_list)
list2_comp = zip(list2, index_list)

list1_sort = sorted(list1_comp)
list2_sort = sorted(list2_comp)

total = 0

for idx, value in enumerate(list1_sort):
    total += abs(value[0]-list2_sort[idx][0])

print("The total distance is: "+str(total))

# Part 2
count_dict1 = {}
count_dict2 = {}

for value in set(list1):
    count_dict1[value] = list1.count(value)

for value in set(list2):
    count_dict2[value] = list2.count(value)

total = 0
for value in list1:
    if value in count_dict2.keys():
        total += value*count_dict2[value]

print("The total distance is: "+str(total))