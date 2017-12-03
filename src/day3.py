from math import ceil, sqrt
from collections import namedtuple
from itertools import count

number = 265149

Step = namedtuple("Step", ["dx", "dy"])
RIGHT = Step(1, 0)
DOWN = Step(0, 1)
LEFT = Step(-1, 0)
UP = Step(0, -1)

def steps_from_center():
    for n in count(start=1):
        if n % 2:
            yield RIGHT
            for _ in range(n):
                yield UP
            for _ in range(n):
                yield LEFT
        else:
            yield LEFT
            for _ in range(n):
                yield DOWN
            for _ in range(n):
                yield RIGHT

square_size = int(ceil(sqrt(number)))
square = [[None] * square_size for _ in range(square_size)]

x0 = y0 = x = y = square_size // 2
square[y][x] = 1

for i, step in enumerate(steps_from_center(), start=2):
    if i > number:
        break
    else:
        x += step.dx
        y += step.dy
        square[y][x] = i

indices = [(ix, iy) for ix, row in enumerate(square) for iy, i in enumerate(row) if i == number]
t1, t2 = indices[0]
print sum([abs(t1 - x0), abs(t2 - y0)])
