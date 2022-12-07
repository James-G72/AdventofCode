move_list = open("Day2_Input.txt").read().split("\n")

#--------  Part 1  ---------
p1_scores = {
    "A X": 4, # Rock = 1, draw = 1
    "A Y": 8, # Paper = 2, win = 6
    "A Z": 3, # Scissors = 3, loss = 0
    "B X": 1, # Rock = 1, loss = 0
    "B Y": 5, # Paper = 2, draw = 3
    "B Z": 9, # Scissors = 3, win = 6
    "C X": 7, # Rock = 1, win = 6
    "C Y": 2, # Paper = 2, loss = 0
    "C Z": 6 # Scissors = 3, draw = 3
}

p1_score = 0
for it in move_list:
    p1_score += p1_scores[it]

print("Part 1: "+str(p1_score))

# --------  Part 2  ---------
p2_scores = {
    "A X": 3, # Scissors = 3, loss = 0
    "A Y": 4, # Rock = 1, draw = 3
    "A Z": 8, # Paper = 2, win = 6
    "B X": 1, # Rock = 1, loss = 0
    "B Y": 5, # Paper = 2, draw = 3
    "B Z": 9, # Scissors = 3, win = 6
    "C X": 2, # Paper = 2, loss = 0
    "C Y": 6, # Scissors = 3, draw = 3
    "C Z": 7 # Rock = 1, win = 6
}

p2_score = 0
for it in move_list:
    p2_score += p2_scores[it]

print("Part 2: "+str(p2_score))