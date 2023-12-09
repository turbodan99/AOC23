#! /usr/bin/env python3

def process_race(time, current_record):
    winners = 0
    for speed in range(0, time + 1):
        remainder = time - speed
        distance_travelled = remainder * speed
        if distance_travelled > current_record:
            winners += 1
    return winners


f = open("input.txt")
lines = f.read().splitlines()
time = int(lines[0].strip("Time:").replace(" ",""))
distance = int(lines[1].strip("Distance:").replace(" ",""))

winners = process_race(time, distance)
print(winners)