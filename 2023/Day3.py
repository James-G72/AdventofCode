
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
    for pos in range(0, len(num)):
        if num[pos].isdigit():
            current_num.append(num[pos])
            if valid_pos[pos]:
                valid = True
        elif valid:
            num_list.append(int("".join(current_num)))
            current_num = []
            valid = False
        else:
            current_num = []
            # Don't think the statement below is entirely necessary but can't hurt
            valid = False
    if valid:
        num_list.append(int("".join(current_num)))
    print(num_list)
    return num_list

line_store = []
for line in open("Day3_input.txt").read().split("\n"):
    line_store.append(line)

total_1 = 0
number_store = [x * (x.isdigit()) for x in line_store[0]]
symbol_store1 = [False for _ in range(0, len(line_store[0]))]
symbol_store2 = [x in SYMBOLS for x in line_store[0]]
symbol_store3 = [x in SYMBOLS for x in line_store[1]]
# Perform calculation for the first line as a special case outside the loop
total_1 += sum(valid_numbers(number_store, symbol_store1, symbol_store2, symbol_store3))
for pos in range(1, len(line_store)-1):
    number_store = [x * (x.isdigit()) for x in line_store[pos]]
    symbol_store1 = [x in SYMBOLS for x in line_store[pos-1]]
    symbol_store2 = [x in SYMBOLS for x in line_store[pos]]
    symbol_store3 = [x in SYMBOLS for x in line_store[pos+1]]
    total_1 += sum(valid_numbers(number_store, symbol_store1, symbol_store2, symbol_store3))
number_store = [x * (x.isdigit()) for x in line_store[-1]]
symbol_store1 = [x in SYMBOLS for x in line_store[-2]]
symbol_store2 = [x in SYMBOLS for x in line_store[-1]]
symbol_store3 = [False for _ in range(0, len(line_store[-1]))]
total_1 += sum(valid_numbers(number_store, symbol_store1, symbol_store2, symbol_store3))

print("Sum of all valid numbers is: " + str(total_1))

# Part 2


def valid_symbols(sym, num1, num2, num3):
    """
    Takes a line of numbers and three lines of symbols and returns all valid numbers as a list.
    :param sym: The position and value of numbers in the line
    :param num1: The symbols in the line above
    :param num2: The symbols in the line
    :param num3: The symbols in the line below
    :return: num_list, all valid numbers in the schematic
    """
    num_list = []
    num_sum = 0
    for i in range(0, len(sym)):
        if sym[i]:
            interesting_positions = [i-1, i, i+1]
            for pos in interesting_positions:
                if num1[pos].isdigit():
                    number_test = num1[pos-2:pos+3]
                    number = test_positions(number_test)
                    if number not in num_list:
                        num_list.append(number)
                if num2[pos].isdigit():
                    number_test = num2[pos-2:pos+3]
                    number = test_positions(number_test)
                    if number not in num_list:
                        num_list.append(number)
                if num3[pos].isdigit():
                    number_test = num3[pos-2:pos+3]
                    number = test_positions(number_test)
                    if number not in num_list:
                        num_list.append(number)
            if len(num_list) == 2:
                gear_ratio = 1
                for i in num_list:
                    gear_ratio *= i
                if gear_ratio < 38420:
                    print(num_list)
                num_sum += gear_ratio
            num_list = []
    print(num_sum)
    return num_sum


def test_positions(number_test):
    number = number_test[2]
    for i in [1, 0]:
        if number_test[i].isdigit():
            number = number_test[i] + number
        else:
            break
    for i in [3, 4]:
        if number_test[i].isdigit():
            number = number + number_test[i]
        else:
            break

    return int(number)


total_2 = 0
idx = 1
symbol_store = []
sums = []
for pos in range(0, len(line_store)):
    line_temp = []
    for i in line_store[pos]:
        if i == '*':
            line_temp.append(idx)
            idx += 1
        else:
            line_temp.append("")
    symbol_store.append(line_temp)
for pos in range(0, len(line_store)):
    if pos == 0:
        prev_line = ["" for _ in range(0, len(line_store[pos]))]
    else:
        prev_line = [x * x.isdigit() for x in line_store[pos-1]]
    current_line = [x * x.isdigit() for x in line_store[pos]]
    if pos == len(line_store)-1:
        next_line = ["" for _ in range(0, len(line_store[pos]))]
    else:
        next_line = [x * x.isdigit() for x in line_store[pos+1]]
    sums.append(valid_symbols(symbol_store[pos], prev_line, current_line, next_line))
total_2 = sum(sums)
print(f"Sum:{total_2}")
