
roll_lines = [x[:-1] for x in open("Day4_input.txt").readlines()]
MAX_COL = len(roll_lines[0])
MAX_ROW = len(roll_lines)

def check_adjacent(full_roll_lines, col_in, row_in):
    if full_roll_lines[row_in][col_in] == ".":
        pass
    else:
        adjacent = 0
        for col in [col_in-1, col_in, col_in+1]:
            if 0 <= col < MAX_COL:
                for row in [row_in-1, row_in, row_in+1]:
                    if 0 <= row < MAX_ROW:
                        adjacent += full_roll_lines[row][col] == "@"
        if adjacent <= 4:
            return 1

    return 0

def remove_rolls(full_rolls):
    total_rolls = 0
    new_rolls = []
    for row_idx, roll_line in enumerate(full_rolls):
        new_roll_row = ""
        for col_idx, space in enumerate(roll_line):
            result = check_adjacent(full_rolls, col_idx, row_idx)
            if result:
                total_rolls += 1
                new_roll_row += "."
            else:
                new_roll_row += space
        new_rolls.append(new_roll_row)

    return total_rolls, new_rolls

def count_rolls(full_rolls):
    rolls = 0
    # print("\nCurrent Roll State:")
    for row in full_rolls:
        # print(row)
        for roll in row:
            rolls += roll == "@"
    return rolls

rolls_removed, roll_lines = remove_rolls(roll_lines)

print("Part1: The sum of invalid entries is: "+str(rolls_removed))

# Part 2

roll_lines = [x[:-1] for x in open("Day4_input.txt").readlines()]

start_rolls = count_rolls(roll_lines)
total_rolls_removed = 0
while 1:
    rolls_removed, roll_lines = remove_rolls(roll_lines)
    total_rolls_removed += rolls_removed
    if count_rolls(roll_lines) == start_rolls:
        break
    else:
        start_rolls = count_rolls(roll_lines)

print("Part2: The sum of invalid entries is: "+str(total_rolls_removed))
