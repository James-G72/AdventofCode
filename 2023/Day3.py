
SYMBOLS = ['%', '/', '-', '*', '$', '&', '+', '#', '=', '@']

def valid_numbers(num, sym1, sym2, sym3):
    """
    Takes a line of numbers and three lines of symbols and returns all valid numbers as a list.
    :param num: The position and value of numbers in the line
    :param sym1: The symbols in the line above
    :param sym2: The symbols in the line
    :param sym3: The symbols in the line below
    :return: num_list, all valid numbers in the schematic
    """
    valid_pos = [False for _ in range(len(num))]
    if any(sym1[0:2]) or any(sym2[0:2]) or any(sym3[0:2]):
        valid_pos[0] = True
    for pos in range(1, len(num)-1):
        if any(sym1[pos-1:pos+2]) or any(sym2[pos-1:pos+2]) or any(sym3[pos-1:pos+2]):
            valid_pos[pos] = True
    if any(sym1[-2:]) or any(sym2[-2:]) or any(sym3[-2:]):
        valid_pos[0] = True

    num_list = []
    current_num = []
    valid = False
    if num[0] != "":
        current_num.append(num[0])
        if valid_pos[0]:
            valid = True
    for pos in range(1, len(num)-1):
        if num[pos] != "":
            current_num.append(num[pos])
            if valid_pos[pos]:
                valid = True
        elif valid:
            _ = ""
            num_list.append(int("".join(map(str,current_num))))
            current_num = []
            valid = False
        else:
            current_num = []
            # Don't think the statement below is entirely necessary but can't hurt
            valid = False
    if num[-1] != "":
        current_num.append(num[-1])
        if valid_pos[-1]:
            valid = True
    elif valid:
        _ = ""
        num_list.append(int("".join(map(str,current_num))))
    if valid:
        _ = ""
        num_list.append(int("".join(map(str,current_num))))
    print(num_list)
    return num_list

line_store = []
for line in open("Day3_input.txt").read().split("\n"):
    line_store.append(line)

total = 0
number_store = [x * (x.isdigit()) for x in line_store[0]]
symbol_store1 = [False for _ in range(0, len(line_store[0]))]
symbol_store2 = [x in SYMBOLS for x in line_store[0]]
symbol_store3 = [x in SYMBOLS for x in line_store[1]]
# Perform calculation for the first line as a special case outside the loop
total += sum(valid_numbers(number_store, symbol_store1, symbol_store2, symbol_store3))
for pos in range(1, len(line_store)-1):
    number_store = [x * (x.isdigit()) for x in line_store[pos]]
    symbol_store1 = [x in SYMBOLS for x in line_store[pos-1]]
    symbol_store2 = [x in SYMBOLS for x in line_store[pos]]
    symbol_store3 = [x in SYMBOLS for x in line_store[pos+1]]
    total += sum(valid_numbers(number_store, symbol_store1, symbol_store2, symbol_store3))
number_store = [x * (x.isdigit()) for x in line_store[-1]]
symbol_store1 = [x in SYMBOLS for x in line_store[-2]]
symbol_store2 = [x in SYMBOLS for x in line_store[-1]]
symbol_store3 = [False for _ in range(0, len(line_store[0]))]
total += sum(valid_numbers(number_store, symbol_store1, symbol_store2, symbol_store3))

print("Sum of all valid numbers is: "+str(total))

