#!/usr/bin/env python3

import lib

def part1(data):
    res = 0
    for c in data:
        if c == "(":
            res += 1
        if c == ")":
            res -= 1
    return res

def part2(data):
    res = 0
    for i in range(len(data)):
        if res == -1:
            return i
        if data[i] == "(":
            res += 1
        if data[i] == ")":
            res -= 1

def main():
    input = lib.read_data("../inputs/01.txt")
    input = input[0]

    res1 = part1(input)
    print("Part 1:", res1)

    res2 = part2(input)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()