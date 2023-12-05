#!/usr/bin/env python3

def gimme(value, conv_map):
    for bracket in conv_map:
        lower = int(bracket.split()[1])
        delta = int(bracket.split()[2])
        output_base = int(bracket.split()[0])
        upper = lower + delta
        if lower <= value <= upper:
            diff = value - lower
            return output_base + diff
    else:
        return value

f = open("input.txt", "r")

file_contents = f.read().split("\n\n")

seeds = (file_contents[0].strip("seeds: ")).split()
seeds_to_soil = (file_contents[1].strip("seed-to-soil map: \n")).split("\n")
soil_to_fertilizer = (file_contents[2].strip("soil-to-fertilizer map: \n")).split("\n")
fertilizer_to_water = (file_contents[3].strip("fertilizer-to-water map: \n")).split("\n")
water_to_light = (file_contents[4].strip("water-to-light map: \n")).split("\n")
light_to_temperature = (file_contents[5].strip("light-to-temperature map: \n")).split("\n")
temperature_to_humidity = (file_contents[6].strip("temperature-to-humidity map: \n")).split("\n")
humidity_to_location = (file_contents[7].strip("humidity-to-location map: \n")).split("\n")

f.close()

locations = []
for seed in seeds:
    val = (int(seed))
    s2s = gimme(val,seeds_to_soil)
    s2f = gimme(s2s, soil_to_fertilizer)
    f2w = gimme(s2f, fertilizer_to_water)
    w2l = gimme(f2w, water_to_light)
    l2t = gimme(w2l, light_to_temperature)
    t2h = gimme(l2t, temperature_to_humidity)
    h2l = gimme(t2h, humidity_to_location)
    locations.append(h2l)

locations.sort()
print(locations[0])
