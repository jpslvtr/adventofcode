#!/usr/bin/env python3

"""Advent of Code 2021 Day 8."""

import numpy as np


def read_file(filename):
    """Return data as formatted."""
    input = open(filename)
    lines = input.readlines()
    return lines


def part1(input):
    """Count 1, 4, 7, and 8."""
    data = []
    for line in input:
        split_line = line.split("|")
        data.append([c for c in split_line[1].split()])
    np.array(data)
    counter = 0
    for i in range(len(data)):
        for x in data[i]:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                counter += 1
    return counter


def part2(input):
    """Count all digits."""
    count = 0
    for line in input:
        code = {}
        jumbled, output_value = line.strip().split('|')
        jumbled = jumbled.split()
        output_value = output_value.split()
        for c in jumbled:
            if len(c) == 7:
                code[8] = ''.join(sorted(c))
            elif len(c) == 4:
                code[4] = ''.join(sorted(c))
            elif len(c) == 3:
                code[7] = ''.join(sorted(c))
            elif len(c) == 2:
                code[1] = ''.join(sorted(c))
        for c in jumbled:
            # if len == 6 , it is 0, 9 or 6
            if len(c) == 6:
                if not all([x in c for x in code[1]]):
                    code[6] = ''.join(sorted(c))
                elif all([x in c for x in code[4]]):
                    code[9] = ''.join(sorted(c))
                else:
                    code[0] = ''.join(sorted(c))
        for c in jumbled:
            # if len == 5, it is 2, 3, or 5
            if len(c) == 5:
                if all([x in c for x in code[1]]):
                    code[3] = ''.join(sorted(c))
                elif all([x in code[9] for x in c]):
                    code[5] = ''.join(sorted(c))
                else:
                    code[2] = ''.join(sorted(c))
        number = ''
        for c in output_value:
            test = ''.join(sorted(c))
            for k in code.keys():
                if code[k] == test:
                    number = ''.join([number, str(k)])
        count += int(number)
    return count


def main():
    """Main."""
    input = read_file('../input/8.txt')
    print(part1(input))
    print(part2(input))


if __name__ == '__main__':
    main()
