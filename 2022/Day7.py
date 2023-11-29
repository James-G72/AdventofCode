info = open("Day5_Input.txt").read().split("\n")

def unpack(new_dir, current_location, whole_drive):
    """
    Takes a list of the contents of a drive and adds it to the drive map
    :param new_dir:
    :param whole_drive:
    :return: whole drive
    """
    return whole_drive

def dir_finder(target, whole_drive):
    """
    Searches the whole drive to find the path to the directory
    :param target:
    :param whole_drive:
    :return: path to the current location
    """

drive = {
    "/":{}
}
listing = False
contents = []
loc = []
for line in info:
    if line[0] == "$":
        if listing:
            drive = unpack(contents)
            contents = []
            listing = False
        if line[2:3] == "cd":
            dir = line.split(" ")[-1]
            if dir == "..":
                loc = loc[:-1]
            else:
                if dir in loc:
                    for x in range(0, len(loc)):
                        if dir == loc[x]:
                            # CHECK THIS IS CORRECT
                            loc = loc[:x]
                        else:
                            loc = dir_finder(dir, drive)
        elif line[2:3] == "ls":
            listing = True
    elif line[0] == "d" or line[0].isdigit():
        contents.append(line)