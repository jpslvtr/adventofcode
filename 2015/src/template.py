#!/usr/bin/env python3

import lib

def read_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def part1(data):
    pass

def part2(data):
    pass

def main():
    input = read_data("../inputs/00.txt")
    
    res1 = part1(input)
    print("Part 1:", res1)
    
    res2 = part2(input)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()