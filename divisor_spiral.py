from ulam import ulam_spiral, factors
colors = ximport('colors')

# Create the Ulam spiral.
grid_size = 31
grid = ulam_spiral(grid_size)

# Fill the grid with the number of factors the integer in the (i,j) position has.
for i in range(grid_size):
    for j in range(grid_size):
        grid[i][j] = len(factors(grid[i][j]))

# Determine the maximum number of factors that one integer in the grid has.
max_d = max(map(max, grid))

# Set up the canvas size.
size(grid_size*max_d, grid_size*max_d)

# Draw a small grid coloring the location of prime numbers.
for i in range(grid_size):
    for j in range(grid_size):
        x = j*max_d
        y = i*max_d
        d = grid[i][j]
        oval(x+(max_d/2. - d/2.), y+(max_d/2. - d/2.), d, d, fill=color(0.0)) 

canvas.save('divisor_spiral.png')
