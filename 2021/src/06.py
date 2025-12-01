#!/usr/bin/env python3

"""Advent of Code 2021 Day 6."""

import numpy as np


def lanternfish(input, days):
    """Simluate landernfish."""
    timer_state = [0]*9
    for time in input:
        timer_state[time] += 1
    print(timer_state)
    for i in range(days):
        new_state = [0]*9
        for i, time in enumerate(timer_state[1:], start=1):
            to_add = timer_state[0]
            new_state[i - 1] = time
        new_state[6] += to_add
        new_state[8] += to_add
        timer_state = new_state
    return sum(timer_state)


def read_file(filename):
    """Return array of coordinates."""
    input = open(filename)
    split = (input.read()).split(",")
    states = np.array([int(c) for c in split], dtype=np.uint8)
    return states


def main():
    """Main."""
    input = read_file('../input/6.txt')
    print(lanternfish(input, days=80))
    print(lanternfish(input, days=256))


if __name__ == '__main__':
    main()
