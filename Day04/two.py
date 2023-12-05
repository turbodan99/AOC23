#!/usr/bin/env python3

games = {}
game_number = 1

# Populate dictionary of games with their numbers and process counter
f = open("input.txt", "r")
for card in f.read().splitlines():
    draw_results = card[10:39].split()
    card_results = card[42:120].split()
    process_count = 1
    games[game_number] = [
        draw_results,
        card_results,
        process_count
    ]
    game_number += 1

# Iterate through the list, updating the process counter of any subsequent cards one
for game in games:
    game_number = game
    draw_results = games[game][0]
    card_results = games[game][1]
    process_count = games[game][2]

    while process_count > 0:
        win_count = 0
        for number in card_results:
            if number in draw_results:
                win_count += 1

        if win_count > 0:
            next_game = game_number + 1
            while win_count > 0:
                games[next_game][2] += 1
                next_game +=1
                win_count -= 1

        process_count -= 1

# Total up the count of each game card
total_cards = 0
for game in games:
    total_cards += games[game][2]

print(total_cards)