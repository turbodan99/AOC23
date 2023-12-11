#! /usr/bin/env python3

file = open("input.txt", "r")
next_values_sum = 0

for history in file.read().splitlines():
    values = history.split()
    int_values = []
    for i in values:
        int_values.append(int(i))
    history_map = {0: int_values}
    all_zeros = False
    count = 1
    while all_zeros is False:
        last_line = history_map[count - 1]
        differences = []
        line_length = len(last_line)
        item_count = 0
        while item_count < line_length - 1:
            differences.append(int(last_line[item_count + 1]) - int(last_line[item_count]))
            item_count += 1
        history_map[count] = differences
        if differences.count(0) == len(differences):
            all_zeros = True
        else:
            count += 1

    levels = len(history_map.keys())
    adjustment_levels = levels - 2
    diff = history_map[adjustment_levels + 1][0]

    while adjustment_levels >= 0:
        new_value = history_map[adjustment_levels][-1] + diff
        history_map[adjustment_levels].append(new_value)
        diff = new_value
        adjustment_levels -= 1

    next_values_sum += diff

print(next_values_sum)




