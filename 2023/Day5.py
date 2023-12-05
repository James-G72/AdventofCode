maps = ["seed_to_soil","soil_to_fert","fert_to_water","water_to_light","light_to_temp","temp_to_humid","humid_to_loc"]
map_dict = dict(zip(maps, [[],[],[],[],[],[],[]]))
map = False
start = 0
for line in open("Day5_input.txt").read().split("\n"):
    if line.split(":")[0] == "seeds":
        seed_ids = [int(x) for x in line.split(":")[1].split(" ") if x != ""]
    if "map" in line.split(":")[0]:
        map = True
        map_type = line.split(":")[0][0:4]
    elif map and line != "":
        column = [x for x in map_dict.keys() if x[0:4] == map_type][0]
        map_dict[column].append([int(x) for x in line.split(" ")])
        start += 1
    else:
        map = False
        start = 0

work_num = 0
locations = []
for seed in seed_ids:
    work_num = seed
    for map_to_check in maps:
        for mapping in map_dict[map_to_check]:
            if work_num >= mapping[1] and work_num < mapping[1]+mapping[2]:
                work_num = mapping[0]+(work_num-mapping[1])
                break

    locations.append(work_num)

print("Lowest location is: "+str(min(locations)))

# Part 2
seeds = []
paired = False
first = 0
for seed in seed_ids:
    if not paired:
        paired = True
        first = seed
    elif paired:
        for addition in range(0,seed):
            seeds.append(first+addition)
        paired = False

print(len(seeds))

work_num = 0
locations = []
for seed in seeds:
    work_num = seed
    for map_to_check in maps:
        for mapping in map_dict[map_to_check]:
            if work_num >= mapping[1] and work_num < mapping[1]+mapping[2]:
                work_num = mapping[0]+(work_num-mapping[1])
                break

    locations.append(work_num)

print("Lowest location is: "+str(min(locations)))