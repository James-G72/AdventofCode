# Solution stolen from https://cutonbuminband.github.io/AOC/qmd/2023.html#day-17-clumsy-crucible

import numpy as np
from queue import PriorityQueue

def navigate(grid, minval=1, maxval=3):
    q = PriorityQueue()
    x_lim = grid.shape[1]-1
    y_lim = grid.shape[0]-1
    goal = [y_lim,x_lim]
    q.put((0,(0,0,0)))
    q.put((0,(0,0,1)))
    seen = set()

    while q:
        cost,(y,x,direction) = q.get()
        if [y,x] == goal:
            break
        if (y,x,direction) in seen:
            continue
        seen.add((y,x,direction))
        original_cost = cost
        for s in [-1,1]:
            cost = original_cost
            new_y,new_x = y,x
            for i in range(1,maxval+1):
                if direction == 1:
                    new_x = x+i * s
                else:
                    new_y = y+i * s
                if new_x < 0 or new_y < 0 or new_x > x_lim or new_y > y_lim:
                    break
                cost += grid[new_y,new_x]
                if ((new_y,new_x,1-direction)) in seen:
                    continue
                if i >= minval:
                    q.put((cost,(new_y,new_x,1-direction)))
    return cost


row_list = []
for line in open("Day17_input.txt"):
    row_list.append([int(x) for x in line.replace("\n","")])
data = np.array(row_list)
print("Part 1: {}".format(navigate(data,1,3)))
