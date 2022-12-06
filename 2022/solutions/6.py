#!/usr/bin/env python3

"""Advent of Code 2022 Day 6."""

from collections import Counter

def read_file(filename):
    with open(filename) as f:
        res = f.read().strip('\n')
    return res

def part1(filename):
    buff = read_file(filename)
    for i in range(len(buff)-3):
        window = buff[i: i+4]
        if len(set(window)) == len(window):
            return i + 4 

def part2(filename):
    buff = read_file(filename)
    for i in range(len(buff)-13):
        window = buff[i: i+14]
        if len(set(window)) == len(window):
            return i + 14

def main():
    inputFile = "../inputs/6.txt"
    print(part1(inputFile))
    print(part2(inputFile))

if __name__ == '__main__':
    main()
