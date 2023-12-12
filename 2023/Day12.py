import itertools

def check_valid(s, summary):
    s_empt = [x for x in s.split(".") if x != ""]
    if len(s_empt) != len(summary):
        return False
    for idx, g in enumerate(s_empt):
        if len(g) != int(summary[idx]):
            return False
    return True

def count_possible(spr, summa):
    internal = 0
    options = [".", "#"]
    q_ms = [(char == "?") for idx,char in enumerate(spr)]
    combi = list(itertools.product([False,True],repeat=sum(q_ms)))
    for comb in combi:
        pos = 0
        temp_spr = ""
        for char in spr:
            if char == "?":
                temp_spr += options[comb[pos]]
                pos += 1
            else:
                temp_spr += char
        if check_valid(temp_spr, summa):
            internal += 1
    return internal

counter = 0
for line in open("Day12_input.txt").read().split("\n"):
    springs, summary = line.split(" ")
    counter += count_possible(springs, summary.split(","))

print("Part 1 total permutations: "+str(counter))

# Part 2
counter = 0
for line in open("Day12_input.txt").read().split("\n"):
    springs, summary = line.split(" ")
    springs = springs+"?"+springs+"?"+springs+"?"+springs+"?"+springs
    summary = summary+","+summary+","+summary+","+summary+","+summary
    counter += count_possible(springs, summary.split(","))

print("Part 2 total permutations: "+str(counter))
