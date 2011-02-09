from ulam import ulam_spiral, factors

# Create the Ulam spiral.
grid_size = 7
grid = ulam_spiral(grid_size)

# Set up the canvas size.
square_size = 50
size(grid_size*square_size, grid_size*square_size)

# Black lines.
stroke(0)

# Set the font properties.
font("Helvetica", 20)
align(align=CENTER)

# Draw a small grid coloring the location of prime numbers.
for i in range(grid_size):
    for j in range(grid_size):
        x = j*square_size
        y = i*square_size
        if len(factors(grid[i][j])) == 2:
            c = color(1.0, 0.0, 0.0, 0.5)
        else:
            c = color(1.0)

        rect(x, y, square_size, square_size, fill=c)
        text(str(grid[i][j]), x, y+square_size/2+8, width=square_size)

canvas.save('small_spiral.png')
