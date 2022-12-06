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
    totalPriority = 0
    sharedKeys = set(first.keys()).intersection(second.keys())
    for key in sharedKeys:
        totalPriority += priority(key) 
    return totalPriority                         

def compare_three_dicts(first, second, third):
    totalPriority = 0
    sharedKeys = set(first.keys()) & set(second.keys()) & set(third.keys())
    for key in sharedKeys:
        totalPriority += priority(key)
    return totalPriority

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
    threeElfGroups = list(grouped(rucksacks, 3))
    for elfGroup in threeElfGroups:
        dict1 = dict.fromkeys(elfGroup[0])
        dict2 = dict.fromkeys(elfGroup[1])
        dict3 = dict.fromkeys(elfGroup[2])
        res += compare_three_dicts(dict1, dict2, dict3)
    return res

def main():
    inputFile = "../inputs/3.txt"
    print(part1(inputFile))
    print(part2(inputFile))

if __name__ == '__main__':
    main()
