#!/usr/bin/env python3

"""Advent of Code 2022 Day 3."""

def read_file(filename):
    with open(filename) as f:
        lines = f.read().split("\n")
    return lines

def priority(c):
    val = ord(c)
    if 97 <= val <= 122:
        val = val - 96
    elif 65 <= val <= 90:
        val = val - 38
    return val

def compare_two_dicts(first, second):
    total_priority = 0
    shared_keys = set(first.keys()).intersection(second.keys())
    for key in shared_keys:
        total_priority += priority(key) 
    return total_priority                         

def compare_three_dicts(first, second, third):
    total_priority = 0
    shared_keys = set(first.keys()) & set(second.keys()) & set(third.keys())
    for key in shared_keys:
        total_priority += priority(key)
    return total_priority

def grouped(l, n): 
    for i in range(0, len(l), n):
        yield l[i:i + n]

def part1(filename):
    res = 0
    rucksacks = read_file(filename)
    for sack in rucksacks:
        length = int(len(sack)/2)
        first = sack[:length]
        second = sack[length:]
        dict1 = dict.fromkeys(first,0)
        dict2 = dict.fromkeys(second,0)
        res += compare_two_dicts(dict1, dict2) 
    return res

def part2(filename):
    res = 0
    rucksacks = read_file(filename)
    three_elf_groups = list(grouped(rucksacks, 3))
    for elf_group in three_elf_groups:
        dict1 = dict.fromkeys(elf_group[0])
        dict2 = dict.fromkeys(elf_group[1])
        dict3 = dict.fromkeys(elf_group[2])
        res += compare_three_dicts(dict1, dict2, dict3)
    return res

def main():
    input_file = "../input/03.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
