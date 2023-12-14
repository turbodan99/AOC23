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

# Remove dummy first row
new_grid = np.delete(grid, 0, axis=0)

# Establish dimensions
rows = new_grid.shape[0]
cols = new_grid.shape[1]

# Identify empty rows
duplicate_rows= []
for row in range(0, rows):
    as_list = list((new_grid[row,:]))
    if as_list.count(".") == cols:
        print("duplicate row")
        duplicate_rows.append(row)

# Duplicate empty columns
duplicate_cols = []
for col in range(0, cols):
    as_list = list((new_grid[:, col]))
    if as_list.count(".") == rows:
        print("duplicate col")
        duplicate_cols.append(col)

print(f"duplicate rows {duplicate_rows} cols {duplicate_cols}")

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
galaxy_progress = len(galaxy_coords)
while len(galaxy_coords) > 1:
    start_galaxy = galaxy_coords[0]
    steps = 0
    for other_galaxy in galaxy_coords[1:]:
        route_steps = nx.bidirectional_shortest_path(G, source=start_galaxy, target=other_galaxy)
        route_steps.remove(start_galaxy) # remove self from steps (start at next one)
        # if any of those rows are in duplicate_rows, add 999999
        add_rows = []
        for r in route_steps:
            row = r[0]
            if row in duplicate_rows and row not in add_rows: # only count each once
                steps += 999999
                add_rows.append(row)
        # if any of those cols are in duplicate_cols, add 999999
        add_cols = []
        for c in route_steps:
            col = c[1]
            if col in duplicate_cols and col not in add_cols: # only count each once
                steps += 999999
                add_cols.append(col)
        steps += len(route_steps)
    overall_steps += steps
    galaxy_coords.pop(0)
    galaxy_progress -= 1

# How many did we find
print(overall_steps)

