#!/usr/bin/env python3

import lib

def part1(data):
    x, y = 0, 0
    visited = set()
    visited.add((x,y))

    for c in data:
        if c == "^":
            y += 1
        elif c == "v":
            y -= 1
        elif c == ">":
            x += 1
        else:
            x -= 1
        visited.add((x,y))
    
    return len(visited)

def part2(data):
    pass

def main():
    input = lib.read_data("../inputs/03.txt")
    input = input[0]

    res1 = part1(input)
    print("Part 1:", res1)
    
    # res2 = part2(input)
    # print("Part 2:", res2)

if __name__ == "__main__":
    main()