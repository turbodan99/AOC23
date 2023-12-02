#! /usr/bin/env python3

def check_round(rounds):
    for reveal in rounds:
        reveal_list = reveal.split(",")
        for balls in reveal_list:
            quantity = int(balls.split()[0])
            colour = balls.split()[1]
            if (colour == "red" and quantity > 12) or (colour == "green" and quantity > 13) or (colour == "blue" and quantity > 14):
                return False
    return True

total = 0
game_counter = 1

f = open("input.txt", "r")
for game in f.read().splitlines():
    shorter = game.split(":")[1]
    rounds = shorter.split(";")
    if check_round(rounds) is False:
        game_counter += 1
    else:
        total += game_counter
        game_counter += 1

print(total)
