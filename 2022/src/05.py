#!/usr/bin/env python3

"""Advent of Code 2022 Day 5."""

import numpy as np
import re

def read_crates(filename):
    crates, res = [], []
    with open(filename) as f:
        for line in f:
            if line[1] == '1':
                break
            line = line.strip('\n').replace('    ', '*')
            line = line.replace('[', '').replace(']', '').replace(' ', '')
            crates.append([*line])
        crates = np.array(crates).T[:,::-1]
    for row in crates:
        newRow = []
        for c in row:
            if c != '*':
                newRow.append(c)
        res.append(newRow)
    return res

def read_moves(filename):
    moves = []
    with open(filename) as f:
       moves = f.readlines()[10:] 
    return moves

def get_input(filename):
    crates = read_crates(filename)
    moves = read_moves(filename)
    return crates, moves 

def part1(filename):
    crates, moves = get_input(filename)
    for line in moves:
        command = list(map(int, re.findall(r'\d+', line)))
        for i in range(command[0]):
            crates[command[2]-1].append(crates[command[1]-1][-1])
            crates[command[1]-1].pop()       
    res = ''.join([c.pop() for c in crates])
    return res

def part2(filename):
    crates, moves = get_input(filename)
    for line in moves:
        command = list(map(int, re.findall(r'\d+', line)))
        crates[command[2]-1].extend(crates[command[1]-1][-command[0]:])
        del crates[command[1]-1][-command[0]:]
    res = ''.join([c.pop() for c in crates])
    return res

def main():
    input_file = "../inputs/05.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
