#! /usr/bin/env python3

import numpy as np

def whats_at(coords):
    x=coords[0]
    y=coords[1]
    return new_grid[x][y]

def adjacents(x, y, xlimit, ylimit):
    left = [x, y - 1]
    right = [x, y + 1]
    above = [x - 1, y]
    below = [x + 1, y]
    up_right = [x - 1, y + 1]
    down_right = [x + 1, y + 1]
    down_left = [x + 1, y - 1]
    up_left = [x - 1, y - 1]
    clean = []
    for coords in left, right, above, below, up_right, down_right, down_left, up_left:
        x = coords[0]
        y = coords[1]
        if x < 0 or y < 0 or x > xlimit or y > ylimit:
            continue
        else:
            clean.append(coords)
    return clean

# Check dimensions of file
lines = 0
line_length = 0
f = open("input.txt", "r")
for line in f.read().splitlines():
    line_length = len(line)
    lines +=1
f.close()

# Create 2D array
grid = np.zeros((1,line_length))

# Populate with data
f = open("input.txt", "r")
for line in f.read().splitlines():
    as_list = list(line)
    grid = np.vstack([grid,as_list])

# Remove dummy first row
new_grid = np.delete(grid, 0, axis=0)

# Find the numbers and their cells
total = 0
for row in range(lines):

    members = []
    building = ""
    active = False
    for col in range(line_length):
        numbers = {}
        if new_grid[row][col] in ["0","1","2","3","4","5","6","7","8","9"] and active == False:
            building = new_grid[row][col]
            members.append([row,col])
            active = True
            if col == line_length - 1:
                numbers[building] = members
                members = []
                active = False
        elif new_grid[row][col] in ["0","1","2","3","4","5","6","7","8","9"] and active == True:
            building = (building + new_grid[row][col])
            members.append([row,col])
            if col == line_length - 1:
                numbers[building] = members
                members = []
                active = False
        elif new_grid[row][col] not in ["0","1","2","3","4","5","6","7","8","9"] and active == True:
            numbers[building] = members
            members = []
            active = False
            building = ""

# For each number, check if any of the digits are adjacent to a symbol, if so, increment the total

        for number in numbers:
            done = False
            for check in numbers[number]:
                x = check[0]
                y = check[1]
                check_these = adjacents(x,y,lines - 1, line_length - 1)
                for chk in check_these:
                    cx = chk[0]
                    cy = chk[1]
                    if new_grid[cx,cy] not in ["0","1","2","3","4","5","6","7","8","9","."] and done == False:
                        total += int(number)
                        done = True
                        break


print(total)

