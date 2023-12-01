#!/usr/bin/env python3

total = 0


f = open("input.txt", "r")
for line in f.read().splitlines():
    start = 0
    while line[start].isdigit() is False:
        start += 1
    first = line[start]

    end = len(line) - 1
    while line[end].isdigit() is False:
        end -= 1
    second = line[end]

    total += (int((first + second)))

print(total)

