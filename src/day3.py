from collections import namedtuple
from itertools import count
from math import ceil, sqrt

INPUT_NUMBER = 265149

Step = namedtuple("Step", ["dx", "dy", "direction"])
RIGHT = Step(1, 0, "Right")
DOWN = Step(0, 1, "Down")
LEFT = Step(-1, 0, "Left")
UP = Step(0, -1, "Up")


def steps_from_center():
    for center_step in count(start=1):
        if center_step % 2:
            yield RIGHT
            for _ in range(center_step):
                yield UP
            for _ in range(center_step):
                yield LEFT
        else:
            yield LEFT
            for _ in range(center_step):
                yield DOWN
            for _ in range(center_step):
                yield RIGHT


def part1():
    square_size = int(ceil(sqrt(INPUT_NUMBER)))
    square_matrix = [[None] * square_size for _ in range(square_size)]

    # find center
    starting_x = starting_y = x = y = square_size // 2
    # fill initial 1
    square_matrix[y][x] = 1

    for index, step in enumerate(steps_from_center(), start=2):
        if index > INPUT_NUMBER:
            break
        else:
            x += step.dx
            y += step.dy
            square_matrix[y][x] = index

        if index == INPUT_NUMBER:
            break

    print sum([abs(x - starting_x), abs(y - starting_y)])


part1()
