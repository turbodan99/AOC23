#! /usr/bin/env python3

def get_max(rounds):
    max = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for reveal in rounds:
        reveal_list = reveal.split(",")
        for balls in reveal_list:
            quantity = int(balls.split()[0])
            colour = balls.split()[1]
            if quantity > max[colour]:
                max[colour] = quantity
    return max

total = 0

f = open("input.txt", "r")
for game in f.read().splitlines():
    shorter = game.split(":")[1]
    rounds = shorter.split(";")
    maxes = get_max(rounds)
    max_power = maxes["red"] * maxes["blue"] * maxes["green"]
    total += max_power

print(total)