#!/usr/bin/env python3

"""Advent of Code 2021 Day 7."""

import numpy as np


def read_file(filename):
    """Return data as formatted."""
    input = open(filename)
    split = (input.read()).split(",")
    return np.array([int(c) for c in split])


def fuel(input):
    """Part 1."""
    positions = sorted(input)
    meeting_point = positions[len(positions)//2]
    return sum([abs(meeting_point-x) for x in positions])


def fuel2(input):
    """Part 2."""
    positions = sorted(input)
    meeting_point = positions[len(positions)//2]
    initial = cost_calc(positions, meeting_point)
    lowest = initial
    for i in range(0, positions[-1]):
        fuel = cost_calc(positions, i)
        if fuel < lowest:
            lowest = fuel
    return lowest


def cost_calc(positions, meeting_point):
    """Cost calculation is Gauss sum per pair."""
    fuel_cost = 0
    for x in positions:
        n = abs(meeting_point-x)
        cost = (n*(n+1))/2
        fuel_cost += cost
    return fuel_cost


def main():
    """Main."""
    input = read_file('../inputs/7.txt')
    part1 = fuel(input)
    print(part1)
    part2 = fuel2(input)
    print(part2)


if __name__ == '__main__':
    main()
