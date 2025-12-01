#!/usr/bin/env python3

"""Advent of Code 2022 Day 13."""

from json import loads
from functools import cmp_to_key

def get_packets(filename):
    with open(filename) as f:
        lines = f.read().replace('\n\n', '\n').splitlines()	
    packets = list(map(loads, lines))
    return packets

def compare(p1, p2):
    p1_int = type(p1) is int
    p2_int = type(p2) is int
    if p1_int and p2_int:
        return p1 - p2
    if p1_int ^ p2_int:
        if p1_int:
            return compare([p1], p2)
        else:
            return compare(p1, [p2])    
    for x, y in zip(p1, p2):
        res = compare(x, y)
        if res != 0:
            return res
    return len(p1) - len(p2)
 
def part1(filename):
    packets = get_packets(filename)
    pairs = []
    res = 0
    for i in range(0, len(packets), 2):
        pairs.append(packets[i:i+2])
    for i, p in enumerate(pairs, 1):
        if compare(*p) < 0:
            res += i
    return res

def part2(filename):
    packets = get_packets(filename)
    packets.extend(([[2]], [[6]]))
    packets.sort(key=cmp_to_key(compare))
    res = packets.index([[2]]) + 1
    res *= packets.index([[6]], res) + 1
    return res

def main():
    input_file = "../input/13.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
	main()
