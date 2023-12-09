#! /usr/bin/env python3

import collections


def numerize(hand):
    sub_hand = []
    new_hand = []
    for i in hand[0]:
        match i:
            case "A":
                val = 14
            case "K":
                val = 13
            case "Q":
                val = 12
            case "J":
                val = 11
            case "T":
                val = 10
            case _:
                val = int(i)
        sub_hand.append(val)
        new_hand = [sub_hand, hand[1]]
    return new_hand


def sort_into_types(rounds):
    for round in rounds:
        round = round.split()
        hand = list(round[0])
        bid = int(round[1])
        distribution = collections.Counter(hand)
        if len(distribution) == 5:  # high card
            high_card.append([hand, bid])
        if len(distribution) == 4:  # pair
            one_pair.append([hand, bid])
        if len(distribution) == 3:  # two pair or 3 of a kind
            if 2 in distribution.values():
                two_pairs.append([hand, bid])
            elif 3 in distribution.values():
                three_of_a_kind.append([hand, bid])
        if len(distribution) == 2:  # full house or 4 of a kind
            if 3 in distribution.values():
                full_house.append([hand, bid])
            else:
                four_of_a_kind.append([hand, bid])
        if len(distribution) == 1:  # 5 of a kind
            five_of_a_kind.append([hand, bid])

    return high_card, one_pair, two_pairs, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind


f = open("input.txt", "r").read()
rounds = (f.splitlines())

high_card = []
one_pair = []
two_pairs = []
three_of_a_kind = []
full_house = []
four_of_a_kind = []
five_of_a_kind = []

sort_into_types(rounds)

overall = []
for type in high_card, one_pair, two_pairs, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind:
    type_sort = []
    for hand in type:
        type_sort.append(numerize(hand))
    type_sort.sort()
    overall += type_sort

count = 1
winnings = 0
for hand in overall:
    winnings += hand[1] * count
    # print(f"{hand[1]} wins {hand[1] * count}")
    count += 1

print(winnings)
