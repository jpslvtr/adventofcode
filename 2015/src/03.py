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
    sx, sy = 0, 0
    rx, ry = 0, 0
    visited = set()
    visited.add((sx,sy))

    santa_turn = True

    for c in data:
        if santa_turn:
            if c == "^":
                sy += 1
            elif c == "v":
                sy -= 1
            elif c == ">":
                sx += 1
            else:
                sx -= 1
            visited.add((sx,sy))
        else:
            if c == "^":
                ry += 1
            elif c == "v":
                ry -= 1
            elif c == ">":
                rx += 1
            else:
                rx -= 1
            visited.add((rx,ry))

        santa_turn = not santa_turn
    
    return len(visited)

def main():
    input = lib.read_data("../inputs/03.txt")
    input = input[0]

    res1 = part1(input)
    print("Part 1:", res1)
    
    res2 = part2(input)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()