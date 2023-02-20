#!/usr/bin/env python3


"""Advent of Code 2022 Day 4."""

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_chunks(line):
    first, second = line.split(',')
    x1, y1 = map(int, first.split('-'))
    x2, y2 = map(int, second.split('-'))
    return x1, y1, x2, y2

def part1(filename):
    lines = read_file(filename)
    res = 0
    for line in lines:
        x1, y1, x2, y2 = get_chunks(line)
        if x1 <= x2 <= y2 <= y1:
            res += 1
        elif x2 <= x1 <= y1 <= y2:
            res += 1
    return res

def part2(filename):
    lines = read_file(filename)
    res = len(lines)
    for line in lines:
        x1, y1, x2, y2 = get_chunks(line)
        if x1 > y2 or x2 > y1:
            res -= 1
    return res

def main():
    input_file = "../inputs/04.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
