a = 0
top_3 = [0, 0, 0]
for x in open("Day1_Input.txt").read().split("\n"):
    if x != "":
        a += int(x)
    else:
        if a > top_3[0]:
            if a > top_3[1]:
                if a > top_3[2]:
                    top_3[0:1] = top_3[1:2]
                    top_3[2] = a
                else:
                    top_3[0] = top_3[1]
                    top_3[1] = a
            else:
                top_3[0] = a
        a = 0

print("The biggest value is: "+str(top_3[2]))

print("The sum of the top three biggest values is: "+str(sum(top_3)))
