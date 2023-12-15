#! /usr/bin/env python3

from more_itertools import distinct_permutations as idp

def list_to_count(listed):
    return_list = []
    count = 0
    process = len(listed)
    for x in listed:
        if x == "#":
            count += 1
            process -=1
            if process == 0:
                return_list.append(count)
        else:
            return_list.append(count)
            count = 0
            process -= 1
    while return_list.count(0) > 0:
        return_list.remove(0)

    return return_list

def generate_options(input, counts):
    find_size = input.count("?")
    target_broken = sum(counts)
    already_found = input.count("#")
    hash_to_find = target_broken - already_found
    dots_left = find_size - hash_to_find
    hashes = '#' * hash_to_find
    dots = '.' * dots_left
    return_list = hashes + dots

    return return_list

def process_options(listed, input, pattern):
    matched = 0

    for option in input:
        listed_temp = listed.copy()
        for i in list(option):
            pos = listed_temp.index("?")
            listed_temp[pos] = i
        if list_to_count(listed_temp) == pattern:
            matched += 1

    return matched

file = open("input.txt", "r")
main_count = 0

for line in file.read().splitlines():
    input = line.split(" ")[0]
    list_input = [*input]
    pattern = ((line.split(" ")[1])).split(",")
    pattern = [int(x) for x in pattern]
    get_options = generate_options(input, pattern)
    options = idp(get_options)
    main_count += process_options(list_input, options, pattern)

print(main_count)

