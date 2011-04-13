from math import pi, sin, cos, atan2, sqrt

WIDTH = 660
HEIGHT = 660

class ArchimedeanSpiral(object):
    """ The Archimedean spiral is the locus of points corresponding to the
    locations over time of a point moving away from a fixed point with a
    constant speed along a line which rotates with constant angular velocity.
    In polar coordinates it is described by:
        r(theta) = a + b*theta, where a,b are Real.

    If we set a = 0 and choose b such that:
        r(2*pi) - r(0) = alpha

    we can write the equations describing the spiral in Cartesian coordinates
    in terms of alpha, the distance between the spirals:
        x(theta) = (alpha * theta) / (2 * pi) * cos(theta)
        y(theta) = (alpha * theta) / (2 * pi) * sin(theta)
    """

    def __init__(self, alpha, num_turns):
        self.alpha = alpha
        self.num_turns = num_turns

    def find_spiral_path(self):
        """ Uses the Nodebox function `findpath` to construct a smooth path
        between a list of points. """
        inc = 0.1
        points = []
        for theta in frange(0, self.num_turns*pi+inc, inc):
            x = (self.alpha * theta) / (2 * pi) * cos(theta)
            y = (self.alpha * theta) / (2 * pi) * sin(theta)
            points.append((x,y))
        return findpath(points)

    def draw_spiral(self, path):
        drawpath(path)

    def draw_rays(self, path, num_rays):
        divisors = []
        for i in range(num_rays):
            divisors.append(len(factors(i)))

        for i, point in enumerate(path.points(amount=num_rays)):
            if i == 0:
                continue
            d = divisors[i]
            oval(point.x-d, point.y-d, 2*d, 2*d)
            theta = atan2(point.y, point.x)
            tx, ty = self.ray_target_point(theta)
            line(point.x, point.y, tx, ty)
            print theta, tx,ty

    def ray_target_point(self, theta):
        """ Given the ray angle, determine the direction to extend the line in. """
        try:
            slope = sin(theta) / cos(theta)
        except ZeroDivisionError:
            slope = 0

        quad = self.find_quadrant(theta)
        if quad == 'QUAD_1':
            tx = WIDTH/2
            ty = slope * tx
            return (tx, ty)
        elif quad == 'QUAD_2':
            tx = -WIDTH/2
            ty = slope * tx
            return (tx, ty)
        elif quad == 'QUAD_3':
            tx = -WIDTH/2
            ty = slope * tx
            return (tx, ty)
        elif quad == 'QUAD_4':
            tx = WIDTH/2
            ty = slope * tx
            return (tx, ty)
        else:
            raise ValueError, "Unknown quadrant"

    def find_quadrant(self, theta):
        """ Assumes that the origin has been set as the center of the figure. """
        if 0 <= theta and theta < pi/2:
            return 'QUAD_1'
        elif pi/2 < theta and theta < pi:
            return 'QUAD_2'
        elif -pi < theta and theta < -pi/2:
            return 'QUAD_3'
        elif -pi/2 < theta and theta < 0:
            return 'QUAD_4'
        else:
            raise ValueError, "Invalid angle."

######## Util functions

def factors(n):
    """ Compute the factors of n. """
    if n == 0: return set()
    return set(reduce(list.__add__, ([i, n/i] for i in xrange(1, int(sqrt(n) + 1)) if n % i == 0)))

def frange(start, end=None, inc=None):
    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while True:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L


######## Begin drawing

colors = ximport('colors')
size(WIDTH, HEIGHT)
translate(WIDTH/2, HEIGHT/2)

nofill()
stroke(0)

spiral = ArchimedeanSpiral(40, 13)
path = spiral.find_spiral_path()
spiral.draw_spiral(path)
spiral.draw_rays(path, 100)

canvas.save('artwork.png')
