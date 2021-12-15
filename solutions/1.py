#!/usr/bin/env python3

"""Advent of Code 2021 Day 1."""

import pandas as pd


def main():
    """Main."""
    depths = pd.read_csv("../inputs/1.txt", header=None).squeeze()

    # Part 1
    increases = sum(depths.diff() > 0)
    print(increases)

    # Part 2
    sum_increases = sum(depths.rolling(3).sum().diff() > 0)
    print(sum_increases)


if __name__ == '__main__':
    main()
