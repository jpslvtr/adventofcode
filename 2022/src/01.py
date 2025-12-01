#!/usr/bin/env python3

"""Advent of Code 2022 Day 1."""

def read_file(filename):
    with open(filename) as f:
        elves = f.read().split("\n\n")   
    return [list(map(int, elf.strip().split("\n"))) for elf in elves]
   
def part1(filename):
    elf_calories = read_file(filename)
    current_max = 0
    for elf in elf_calories:
        if current_max <= sum(elf):
            current_max = sum(elf)
    return current_max
 
def part2(filename):
    elf_calories = read_file(filename)
    total_calories = []
    for elf in elf_calories:
        total_calories.append(sum(elf))
    return sum(sorted(total_calories, reverse=True)[0:3]) 

def main():
    input_file = "../input/01.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
