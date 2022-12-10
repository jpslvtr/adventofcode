#!/usr/bin/env python3

"""Advent of Code 2022 Day 10."""

signal1, signal2 = 1, 1
cycle1, cycle2 = 0, 0
crt = []
res1, res2 = 0, ''

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def next_inst():
    global cycle1, res1
    cycle1 += 1
    if cycle1 in (20, 60, 100, 140, 180, 220):
       res1 += (cycle1 * signal1)

def next_draw():
    global signal2, cycle2, res2
    row = cycle2 // 40
    col = cycle2 % 40
    if abs(signal2 - col) <= 1:
        crt[row][col] = '#'
    cycle2 += 1

def part1(filename):
    global signal1, res1
    lines = read_file(filename)
    for line in lines:
        line = line.split()
        if line[0] == "noop":
            next_inst()
        else:
            next_inst()
            next_inst()
            signal1 += int(line[1])
    return res1

def part2(filename):
    global signal2, crt, res2
    lines = read_file(filename)
    for row in range(0, 6):
        crt.append([])
        for col in range(0, 40):
            crt[row].append('.')
    for line in lines:
        line = line.split()
        if line[0] == "noop":
            next_draw()
        else:
            next_draw()
            next_draw()
            signal2 += int(line[1])
    for row in range(0, 6):
        res2 += (''.join(crt[row]) + '\n')
    return res2

def main():
    input_file = "../inputs/10.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
