#!/usr/bin/env python3

file = open("input.txt", "r")

directions = (file.read().splitlines()[0])
file.close()

instructions = {}
file = open("input.txt", "r")
for line in (file.read().splitlines()[2:]):
    node = line.split("=")[0].strip(" ")
    left_right = line.split("=")[1]
    left_right = (left_right.strip(" ()")).split(", ")
    instructions[node] = left_right

target_node = "AAA"
count = 0
finished = False

while finished is not True:
    for direction in directions:
        if direction == "L":
            next_node = instructions[target_node][0]  # Left
        else:
            next_node = instructions[target_node][1]  # Right
        if next_node == "ZZZ":
            finished = True
        else:
            count += 1
            target_node = next_node

print(f"Finished, ZZZ is at {count + 1}")
