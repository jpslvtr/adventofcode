#!/usr/bin/env python3

"""Advent of Code 2021 Day 3."""

import numpy as np


class Counter:
    """Class Counter."""

    zeros = 0
    ones = 0

    def common(self):
        """Return most common bit."""
        return 0 if self.zeros > self.ones else 1

    def least_common(self):
        """Return least common bit."""
        return 1 if self.zeros > self.ones else 0


def read_file(filename):
    """Take input; return np array."""
    data = np.loadtxt(filename, dtype='str')
    return data


def binary_to_decimal(string):
    """Take a binary number, its decimal equivalent."""
    res = 0
    for i, bit in enumerate(string[::-1]):
        if int(bit) == 1:
            res = res + pow(2, i)
    return res


def power_consumption(input):
    """Find power consumption."""
    counts = [Counter() for i in range(len(input[0]))]
    for report in input:
        for i, bit in enumerate(report):
            if bit == "0":
                counts[i].zeros += 1
            elif bit == "1":
                counts[i].ones += 1
    gamma = "".join([str(count.common()) for count in counts])
    epsilon = "".join([str(count.least_common()) for count in counts])
    gamma_rate = binary_to_decimal(gamma)
    epsilon_rate = binary_to_decimal(epsilon)
    return gamma_rate * epsilon_rate


def rating(input, type, index):
    """Find oxygen generator and CO2 scrubber ratings."""
    if len(input) == 1:
        return binary_to_decimal(input[0])
    counts = [Counter() for i in range(len(input[0]))]
    for report in input:
        for i, bit in enumerate(report):
            if bit == "0":
                counts[i].zeros += 1
            elif bit == "1":
                counts[i].ones += 1
            else:
                raise ValueError()
    gamma = "".join([str(count.common()) for count in counts])
    if "oxygen" == type:
        return rating(
            [report for report in input if report[index] == gamma[index]],
            type, index + 1)
    else:
        return rating(
            [report for report in input if report[index] != gamma[index]],
            type, index + 1)


def life_support_rating(input):
    """Obtain life support rating."""
    oxygen = rating(input, "oxygen", 0)
    co2 = rating(input, "co2", 0)
    return oxygen * co2


def main():
    """Main."""
    input = read_file('../input/3.txt')
    print(power_consumption(input))
    print(life_support_rating(input))


if __name__ == '__main__':
    main()
