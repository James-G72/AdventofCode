impossible_sum = 0
cube_dict = {"red":12, "green":13, "blue":14}

for line in open("Day2_input.txt").read().split("\n"):
    front, back = line.split(":")
    game_id = front.split(" ")[1]
    possible = True
    for show in back.split(";"):
        for cubes in show.split(","):
            if int(cubes.split(" ")[1]) > cube_dict[cubes.split(" ")[-1]]:
                possible = False
    if possible:
        impossible_sum += int(game_id)

print("Total sum of impossible games: "+str(impossible_sum))

# Part 2
power_sum = 0
cube_dict = {"red":0, "green":1, "blue":2}

for line in open("Day2_input.txt").read().split("\n"):
    back = line.split(":")[1]
    cube_list = [0, 0, 0]
    for show in back.split(";"):
        for cubes in show.split(","):
            if int(cubes.split(" ")[1]) > cube_list[cube_dict[cubes.split(" ")[-1]]]:
                cube_list[cube_dict[cubes.split(" ")[-1]]] = int(cubes.split(" ")[1])
    game_power = cube_list[0]*cube_list[1]*cube_list[2]
    power_sum += game_power

print("Total sum of impossible games: "+str(power_sum))