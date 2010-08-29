#!/usr/bin/env python

from random import randint
import png

# Initialize a grid with all zeros.
grid_size = 16
grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

# Fill the grid with the increasing integers spiraling outwards from the center.
idx = 0
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        grid[i][j] = idx
        idx += 1

# Create an 8-bit color palette (256 unique colors).
palette = []
for i in range(156):
    r,g,b = i,i,i
    palette.append((r,g,b))

print palette


f = open('palette_test.png', 'wb')
w = png.Writer(len(grid[0]), len(grid), palette=palette, bitdepth=8)
w.write(f, grid)
f.close()
