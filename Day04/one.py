#!/usr/bin/env python3

total_score = 0

f = open("input.txt", "r")
for card in f.read().splitlines():
    draw_results = card[10:39].split()
    card_results = card[42:120].split()

    hits = 0
    for result in card_results:
        if result in draw_results:
            hits +=1

    card_score = 0
    if hits > 0:
        card_score = 2 ** (hits - 1)
        total_score += card_score

print(total_score)