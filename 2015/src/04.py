#!/usr/bin/env python3

import lib
import hashlib

def part1(data):
    integer = 1
    while True:
        combo = data + str(integer)
        md5hash = hashlib.md5(combo.encode()).hexdigest()
        if md5hash.startswith("00000"):
            return integer
        integer += 1

def part2(data):
    integer = 1
    while True:
        combo = data + str(integer)
        md5hash = hashlib.md5(combo.encode()).hexdigest()
        if md5hash.startswith("000000"):
            return integer
        integer += 1

def main():
    input = lib.read_data("../input/04.txt")
    input = input[0]

    res1 = part1(input)
    print("Part 1:", res1)
    
    res2 = part2(input)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()