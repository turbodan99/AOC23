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
times = (lines[0].strip("Time:").split())
distances = (lines[1].strip("Distance:").split())

results = 1
for i in range(0, len(times)):
    results *= (process_race(int(times[i]), int(distances[i])))
print(results)
