#!/usr/bin/env python3

"""Advent of Code 2021 Day 2."""

import numpy as np

x = 0
y = 0
aim = 0


def read_file(filename):
    """Take input; return np array."""
    data = np.loadtxt(filename, dtype='str')
    return data


def get_coordinates(positions):
    """Take np array, return vertical and horizontal positions."""
    global x, y
    for position in positions:
        if position[0] == 'down':
            x += int(position[1])
        elif position[0] == 'up':
            x -= int(position[1])
        elif position[0] == 'forward':
            y += int(position[1])
    return x, y


def get_actual_coordinates(positions):
    """Take np array, return vertical and horizontal positions."""
    global x, y, aim
    for position in positions:
        if position[0] == 'down':
            aim += int(position[1])
        elif position[0] == 'up':
            aim -= int(position[1])
        elif position[0] == 'forward':
            x += int(position[1])
            y += aim*int(position[1])
    return x, y


def main():
    """Main."""
    positions = read_file('../input/2.txt')
    part1 = get_coordinates(positions)
    print(part1)
    part2 = get_actual_coordinates(positions)
    print(part2)


if __name__ == '__main__':
    main()
