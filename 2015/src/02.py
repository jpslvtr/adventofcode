#!/usr/bin/env python3

import lib

def part1(data):
    res = 0
    for dim in data:
        l = int(dim.split("x")[0])
        w = int(dim.split("x")[1])
        h = int(dim.split("x")[2])
        lw, wh, hl = l*w, w*h, h*l
        area = 2*lw + 2*wh + 2*hl + min(lw, wh, hl)
        res += area
    return res

def part2(data):
    res = 0
    for dim in data:
        dim = dim.split("x")
        l, w, h = map(int, dim)
        sides = sorted([l, w, h])
        wrap = 2*sides[0] + 2*sides[1]
        bow = l*w*h
        res += (wrap + bow)
    return res

def main():
    input = lib.read_data("../inputs/02.txt")

    res1 = part1(input)
    print("Part 1:", res1)
    
    res2 = part2(input)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()