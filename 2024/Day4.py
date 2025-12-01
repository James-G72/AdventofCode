
total = 0
whole_dict = {}
line_stack = []


def search_xmas(line_stack, row, col):
    """
    Check all valid research combinations around X.
    :return:
    """
    row_limit = len(line_stack[0])
    col_limit = len(line_stack)
    indexes = [
        [[0, 1, 2, 3], [0, 0, 0, 0]],
        [[0,-1,-2,-3],[0,0,0,0]],
        [[0,0,0,0], [0,-1,-2,-3]],
        [[0,0,0,0],[0,1,2,3]],
        [[0,1,2,3],[0,-1,-2,-3]],
        [[0,-1,-2,-3],[0,-1,-2,-3]],
        [[0,-1,-2,-3],[0,1,2,3]],
        [[0,1,2,3],[0,1,2,3]]
    ]
    xmas_count = 0
    for rows, columns in indexes:
        string = ""
        try:
            for x in range(0, len(rows)):
                assert all([row+rows[x] >=0, col+columns[x] >=0, row+rows[x] <= row_limit, col+columns[x] <= col_limit])
                string += line_stack[row+rows[x]][col+columns[x]]
        except:
            pass
        if string == "XMAS" or string == "SAMX":
            xmas_count += 1
    return xmas_count

def search_x_mas(line_stack,row,col):
    """
    Check all valid research combinations around A.
    :return:
    """
    row_limit = len(line_stack[0])
    col_limit = len(line_stack)
    indexes = [
        [[-1, 1], [1, -1]],
        [[-1, 1], [-1, 1]],
        ]
    diag = ["", ""]
    idx = 0
    for rows,columns in indexes:
        try:
            for x in range(0,len(rows)):
                assert all([row+rows[x] >= 0,col+columns[x] >= 0,row+rows[x] <= row_limit,col+columns[x] <= col_limit])
                diag[idx] += line_stack[row+rows[x]][col+columns[x]]
        except:
            pass
        idx += 1
    if all([(x == "MS" or x == "SM") for x in diag]):
        return 1
    return 0


for row, line in enumerate(open("Day4_input.txt").read().split("\n")):
    whole_dict[row] = line
    line_stack.append(line)

total = 0
for row, line in enumerate(line_stack):
    for col, char in enumerate(line):
        if char == "X":
            total += search_xmas(line_stack, row, col)

print("Total number of XMASes is: "+str(int(total)))

# Part 2

total = 0
for row, line in enumerate(line_stack):
    for col, char in enumerate(line):
        if char == "A":
            total += search_x_mas(line_stack, row, col)

print("Total number of X-MASes is: "+str(int(total)))
