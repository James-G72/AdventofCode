
SYMBOLS = ['%', '/', '-', '*', '$', '&', '+', '#', '=', '@']

line_store = []
for line in open("Day3_input.txt").read().split("\n"):
    line_store.append(line)

number_store1 = [iter*(x.isdigit()) for iter, x in enumerate(line_store[0])]
number_store2 = []
number_store3 = []
symbol_store1 = [iter*(x in SYMBOLS) for iter, x in enumerate(line_store[0])]
symbol_store2 = []
symbol_store3 = []
width = len(line_store[0])
for pos in range(1, len(line_store)):
    symbol_store1 = [iter*(x in SYMBOLS) for iter, x in enumerate(line_store[pos-1])]
    symbol_store2 = [iter * (x in SYMBOLS) for iter,x in enumerate(line_store[pos])]
    symbol_store3 = [iter * (x in SYMBOLS) for iter,x in enumerate(line_store[pos+1])]
    number_store1 = [iter*(x.isdigit()) for iter, x in enumerate(line_store[pos-1])]
    number_store2 = [iter * (x.isdigit()) for iter,x in enumerate(line_store[pos])]
    number_store3 = [iter * (x.isdigit()) for iter,x in enumerate(line_store[pos+2])]
    t = 1
