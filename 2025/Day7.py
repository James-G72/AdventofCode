from xarray.core.formatting import last_item

lines = []
for line in open("Day7_input.txt").readlines():
        lines.append(line.split("\n")[0])

beam_index = [lines[0].index("S")]
splits = 0
for idx_row, line in enumerate(lines[1:]):
    next_beam_index = []
    for idx_col, char in enumerate(line):
        if char == "^" and idx_col in beam_index:
            real_split = 0
            if idx_col-1 >= 0 and line[idx_col-1] == ".":
                next_beam_index.append(idx_col-1)
                real_split = 1
            if idx_col+1 <= len(line) and line[idx_col+1] == ".":
                next_beam_index.append(idx_col+1)
                real_split = 1
            if real_split:
                splits += 1
        elif idx_col in beam_index:
            next_beam_index.append(idx_col)
    beam_index = next_beam_index

print("Part1: The sum of invalid entries is: "+str(splits))

# Part 2

ALL_LINES = lines[1:]
TIMELINES = 0
beam_index = lines[0].index("S")

def track_beam(row, beam_idx):
    if row >= len(ALL_LINES)-1:
        last_row = True
    else: last_row = False
    global TIMELINES
    char_row = ALL_LINES[row]
    if char_row[beam_idx] == "^":
        if beam_idx-1 >= 0 and char_row[beam_idx-1] == ".":
            if last_row:
                TIMELINES += 1
            else:
                track_beam(row+1, beam_idx-1)
        if beam_idx+1 <= len(char_row) and char_row[beam_idx+1] == ".":
            if last_row:
                TIMELINES += 1
            else:
                track_beam(row+1, beam_idx+1)
    else:
        if last_row:
            TIMELINES += 1
        else:
            track_beam(row+1, beam_idx)

track_beam(0, beam_index)

print("Part2: The sum of invalid entries is: "+str(TIMELINES))