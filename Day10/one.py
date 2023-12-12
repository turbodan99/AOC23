#! /usr/bin/env python3

import numpy as np


def available_directions(current_position, limit):
    my_ok = []
    x_pos = current_position[0]
    y_pos = current_position[1]
    current_value = big_grid[current_position]

    match current_value:
        case "|":
            my_ok = [(x_pos - 1, y_pos), (x_pos + 1, y_pos)]
        case "-":
            my_ok = [(x_pos, y_pos - 1), (x_pos, y_pos + 1)]
        case "J":
            my_ok = [(x_pos - 1, y_pos), (x_pos, y_pos - 1)]
        case "F":
            my_ok = [(x_pos + 1, y_pos), (x_pos, y_pos + 1)]
        case "7":
            my_ok = [(x_pos + 1, y_pos), (x_pos, y_pos - 1)]
        case "L":
            my_ok = [(x_pos - 1, y_pos), (x_pos, y_pos + 1)]
        case "S":
            my_ok = [(x_pos - 1, y_pos), (x_pos + 1, y_pos), (x_pos, y_pos - 1), (x_pos, y_pos + 1)]

    for cell in my_ok:
        if limit >= cell[0] >= 0 and limit >= cell[1] >= 0 and big_grid[cell] not in ["."]:
            continue
        else:
            my_ok.remove(cell)

    return my_ok


file = open("input.txt", "r")

big_list = []
for i in file.read().splitlines():
    big_list.append(list(i))

big_grid = np.array(big_list)
limit = big_grid.shape[0] - 1
start_position = np.where(big_grid == "S")
start_xy = (start_position[0][0], start_position[1][0])

position_log = [start_xy]
next_position = available_directions(start_xy, limit)[0]

loop_complete = False
while loop_complete is False:
    position_log.append(next_position)
    options = available_directions(next_position, limit)
    if start_xy in options:
        options.remove(start_xy)
    if len(options) == 1 and options[0] in position_log:
        loop_complete = True
        break
    else:
        for position in options:
            if position not in position_log:
                next_position = position

print(len(position_log) / 2)
