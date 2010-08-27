from itertools import chain

# Square length must be odd.
x_coords = [[0]]
y_coords = [[0]]
for i, n in enumerate(xrange(3, 9, 2)):
    seq1 = [n-(2+i) for x in xrange(n)]
    seq2 = [x-(i+1) for x in reversed(xrange(n))]
    seq3 = [(2+i)-n for x in xrange(n)]
    seq4 = [x-(i+1) for x in xrange(n)]
    x_coords.append(seq1[1:] + seq2[1:] + seq3[1:] + seq4[1:])
    y_coords.append(seq4[1:] + seq1[1:] + seq2[1:] + seq3[1:])

print list(chain.from_iterable(x_coords))
print list(chain.from_iterable(y_coords))
