from __future__ import division
from ulam import ulam_spiral, factors

# Create the Ulam spiral.
grid_size = 11
grid = ulam_spiral(grid_size)

# Set up the canvas size.
square_size = 50
size(grid_size*square_size, grid_size*square_size)

# Black lines.
stroke(0)

# Set the font properties.
font("Helvetica", 20)
align(align=CENTER)


# x = [[1,2,3], [4,5,6], [7,8,9]]
# n = 3
# for i in range(2*n-1):
    # if i < n:
        # z = 0
    # else:
        # z = i-n+1
    # tmp = []
    # for j in range(z, i-z+1):
        # tmp.append(x[j][i-j])
    # print "Slice %s: %s" % (i, tmp)
        
def count_primes(x):
    count = 0
    for e in x:
        if len(factors(e)) == 2:
            count += 1
    return count

density = {}
for i in range(0, 2 * grid_size - 1):
    if i < grid_size:
        z = 0
    else:
        z = i - grid_size + 1

    diag = []
    for j in range(z, i - z + 1):
        diag.append(grid[j][i-j])

    density[i] = count_primes(diag) / len(diag)


for i in range(0, 2 * grid_size - 1):
    if i < grid_size:
        z = 0
    else:
        z = i - grid_size + 1

    for j in range(z, i - z + 1):
        x = (i-j)*square_size
        y = j*square_size
        c = color(density[i]+0.1)
        rect(x, y, square_size, square_size, fill=c)
        text(str(grid[j][i-j]), x, y+square_size/2+8, width=square_size)
print "done."

canvas.save('colored_spiral.png')
