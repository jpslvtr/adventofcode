#!/usr/bin/env python3

"""Advent of Code 2021 Day 5."""

import numpy as np
from collections import namedtuple


def read_file(filename):
    """Return array of coordinates."""
    Line = namedtuple("Line", "x1 y1 x2 y2")
    mytuples = []
    with open(filename, 'r') as f:
        for line in f:
            raw = [line.split(",") for line in line.strip().split(" -> ")]
            (x1, y1), (x2, y2) = raw
            mytuple = Line(int(x1), int(y1), int(x2), int(y2))
            mytuples.append(mytuple)
    return mytuples


def overlap(input):
    """Count overlap for vertical and horizontal lines."""
    max_x = max(max(line.x1, line.x2) for line in input)
    max_y = max(max(line.y1, line.y2) for line in input)
    grid = np.zeros(shape=(max_x+1, max_y+1), dtype="int16")

    for x1, y1, x2, y2 in input:
        if (x1 == x2) or (y1 == y2):
            if (x1 < x2) or (y1 < y2):
                grid[x1: x2+1, y1: y2+1] += 1
            elif (x1 > x2) or (y1 > y2):
                grid[x2: x1+1, y2: y1+1] += 1
    overlap_count = np.count_nonzero(grid > 1)
    return overlap_count, grid


def overlap_diagonal(input, grid):
    """Consider diagonal lines as well."""
    for x1, y1, x2, y2 in input:
        if (x1 != x2) and (y1 != y2):
            x_dir = -1 if x1 > x2 else 1
            y_dir = -1 if y1 > y2 else 1
            dist = zip(range(x1, x2+x_dir, x_dir), range(y1, y2+y_dir, y_dir))
            for x, y in dist:
                grid[x, y] += 1
    overlap_count = np.count_nonzero(grid > 1)
    return overlap_count


def main():
    """Main."""
    input = read_file('../input/5.txt')
    part1, grid = overlap(input)
    print(part1)
    part2 = overlap_diagonal(input, grid)
    print(part2)


if __name__ == '__main__':
    main()
