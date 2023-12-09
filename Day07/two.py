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
                if hand[2] is True:  # Jack has been used as wildcard so loses value
                    val = 0
                else:
                    val = 11
            case "T":
                val = 10
            case _:
                val = int(i)
        sub_hand.append(val)
        new_hand = [sub_hand, hand[1]]
    return new_hand


def process_jack(distribution):
    # is the jack (one of) the most frequent
    highest_frequency = max(distribution.values())
    if distribution["J"] == highest_frequency:
        return True
    else:
        return False


def sort_into_types(rounds):
    for round in rounds:
        round = round.split()
        hand = list(round[0])
        bid = int(round[1])
        distribution = collections.Counter(hand)
        if len(distribution) == 5:  # high card
            if "J" in distribution.keys():
                one_pair.append([hand, bid, True])  # high jack can make a pair
            else:
                high_card.append([hand, bid, False])
        if len(distribution) == 4:  # pair
            if "J" in distribution.keys():
                three_of_a_kind.append([hand, bid, True])  # if there is a jack or pair of, another val can make a 3oak
            else:
                one_pair.append([hand, bid, False])
        if len(distribution) == 3:  # two pair or 3 of a kind
            if 2 in distribution.values():  # it's two pair
                if "J" in distribution.keys():
                    if process_jack(
                            distribution) is True:  # we have two pair, one is jacks, they can join the other pair
                        four_of_a_kind.append([hand, bid, True])
                    else:
                        full_house.append([hand, bid, True])  # the jack can make it a full house
                else:
                    two_pairs.append([hand, bid, False])
            elif 3 in distribution.values():  # it's a 3oak
                if "J" in distribution.keys():
                    four_of_a_kind.append([hand, bid, True])  # the jack(s) can join to make it a 4oak
                else:
                    three_of_a_kind.append([hand, bid, False])
        if len(distribution) == 2:  # full house or 4 of a kind
            if 3 in distribution.values():  # full house
                if "J" in distribution.keys():
                    five_of_a_kind.append([hand, bid, True])  # the jacks can make it a 5oak
                else:
                    full_house.append([hand, bid, False])
            else:  # four of a kind
                if "J" in distribution.keys():
                    five_of_a_kind.append([hand, bid, True])  # the jack(s) can make it a 5oak
                else:
                    four_of_a_kind.append([hand, bid, False])
        if len(distribution) == 1:  # 5 of a kind
            if "J" in distribution.keys():
                five_of_a_kind.append([hand, bid, True])  # five jacks lose their value
            else:
                five_of_a_kind.append([hand, bid, False])

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
    count += 1

print(winnings)
