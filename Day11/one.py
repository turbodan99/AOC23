#! /usr/bin/env python3

import numpy as np
import networkx as nx  # Lifesaver

# Check dimensions of file
lines = 0
line_length = 0
f = open("input.txt", "r")
for line in f.read().splitlines():
    line_length = len(line)
    lines += 1
f.close()

# Create 2D array with dummy first row
grid = np.zeros((1, line_length))

# Populate with real data
f = open("input.txt", "r")
for line in f.read().splitlines():
    as_list = list(line)
    grid = np.vstack([grid, as_list])
    if as_list.count(".") == line_length:  # Duplicate empty rows
        grid = np.vstack([grid, as_list])

# Remove dummy first row
new_grid = np.delete(grid, 0, axis=0)

# Establish dimensions
rows = new_grid.shape[0]
cols = new_grid.shape[1]

# Duplicate empty columns
duplicate_pos = []
for col in range(0, cols):
    as_list = list((new_grid[:, col]))
    if as_list.count(".") == rows:
        duplicate_pos.append(col)

for col in reversed(duplicate_pos):
    new_grid = np.insert(new_grid, col, ".", axis=1)

# Establish revised dimensions
rows = new_grid.shape[0]
cols = new_grid.shape[1]

# Find galaxies and their co-ordinates
galaxies = np.where(new_grid == "#")
galaxy_count = len(galaxies[0])

galaxy_coords = []
for i in range(0, galaxy_count):
    x = galaxies[0][i]
    y = galaxies[1][i]
    galaxy_coords.append((x, y))

# Create the grid for networkx
G = nx.grid_2d_graph(rows, cols)

# Count every path from first position, then bump it and go again
overall_steps = 0
while len(galaxy_coords) > 1:
    start_galaxy = galaxy_coords[0]
    steps = 0
    for other_galaxy in galaxy_coords[1:]:
        route_steps = len(
            nx.bidirectional_shortest_path(G, source=start_galaxy, target=other_galaxy)) - 1  # remove starting position
        steps += route_steps
    overall_steps += steps
    galaxy_coords.pop(0)

# How many did we find
print(overall_steps)
