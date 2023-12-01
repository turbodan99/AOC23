#!/usr/bin/env python3

total = 0
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def convert(word):
    match word.lower():
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"


f = open("input.txt", "r")
for line in f.read().splitlines():
    start = 0
    first = ""
    while line[start].isdigit() is False:
        sub_line = line[0:start + 1]
        for word in words:
            if word in sub_line:
                first = convert(word)
        if first != "":
            break
        else:
            start += 1
    if first == "":
        first = line[start]

    end = len(line) - 1
    second = ""
    while line[end].isdigit() is False:
        sub_line = line[end:]
        for word in words:
            if word in sub_line:
                second = convert(word)
        if second != "":
            break
        else:
            end -= 1
    if second == "":
        second = line[end]

    total += (int((first + second)))

print(total)
