import png
from math import sqrt
from itertools import chain

def print_grid(grid):
    """ Pretty print the grid with the proper spacing. """
    max_element = max(max(grid))
    num_digits = len(str(max_element))
    for row in grid:
        row = map(lambda x: str(x).rjust(num_digits, ' '), row)
        print ' '.join(row)

def generate_coords(grid_size):
    """ Compute the cartesian (x, y) coordinates for the Ulam spiral entries.  grid_size must be odd. """
    x_coords = [[0]]
    y_coords = [[0]]
    for i, n in enumerate(xrange(3, grid_size, 2)):
        seq1 = [n-(2+i) for x in xrange(n)]
        seq2 = [x-(i+1) for x in reversed(xrange(n))]
        seq3 = [(2+i)-n for x in xrange(n)]
        seq4 = [x-(i+1) for x in xrange(n)]
        x_coords.append(seq1[1:] + seq2[1:] + seq3[1:] + seq4[1:])
        y_coords.append(seq4[1:] + seq1[1:] + seq2[1:] + seq3[1:])

    x_coords = list(chain.from_iterable(x_coords))
    y_coords = list(chain.from_iterable(y_coords))
    coords = zip(x_coords, y_coords)

    return coords

def factors(n):
    """ Compute the factors of n. """
    return set(reduce(list.__add__, ([i, n/i] for i in xrange(1, int(sqrt(n) + 1)) if n % i == 0)))


# Compute the coordinates. NOTE: Actual grid size will be x - 2.
grid_size = 4999
coords = generate_coords(grid_size)

# Initialize a grid with all zeros.
grid = [[0 for i in range(grid_size-2)] for j in range(grid_size-2)]

# Fill the grid with the increasing integers spiraling outwards from the center.
for i, c in enumerate(coords):
    x = c[0] + (grid_size // 2) - 1
    y = c[1] + (grid_size // 2) - 1
    grid[y][x] = i+1

# Replace grid integers with the total number of divisors each integer has.
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        grid[i][j] = len(factors(val))

# Create an 8-bit color palette (256 unique colors).
palette = []
for i in range(156):
    r,g,b = int(i,i,i
    palette.append((r,g,b))
# palette = []
# for i in range(16, 200):
    # r = int(float(i) / (239.0 - 16.0) * 90.0)
    # g = int(float(i) / 128.0 * 90.0)
    # b = 100
    # palette.append((r,g,b))

f = open('spiral.png', 'wb')
w = png.Writer(len(grid[0]), len(grid), palette=palette, bitdepth=8)
w.write(f, grid)
f.close()





######
# Binary Ulam Spiral, with primes = white, composite = black.

# Replace grid values with 0 for composite numbers and 1 for primes.
# for i, row in enumerate(grid):
    # for j, val in enumerate(row):
        # if len(factors(val)) == 2:
            # grid[i][j] = 1
        # else:
            # grid[i][j] = 0

# Use PyPNG to write a binary image.
# f = open('spiral.png', 'wb')
# w = png.Writer(len(grid[0]), len(grid), greyscale=True, bitdepth=1)
# w.write(f, grid)
# f.close()
