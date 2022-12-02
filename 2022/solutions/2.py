#!/usr/bin/env python3

"""Advent of Code 2022 Day 2."""

game = { 
    "A X" : 4,
    "A Y" : 8,
    "A Z" : 3,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6
}

decrypt = {
    "A X" : "A Z",
    "A Y" : "A X",
    "A Z" : "A Y",
    "B X" : "B X",
    "B Y" : "B Y",
    "B Z" : "B Z",
    "C X" : "C Y",
    "C Y" : "C Z",
    "C Z" : "C X"
}

def read_file(filename):
    with open(filename) as f:
        moves = f.read().split("\n")
    return moves

def part1(filename):
    moves = read_file(filename)
    score = 0
    for line in moves:
        score += game[line]
    return score 
 
def part2(filename):
    moves = read_file(filename)
    score = 0
    for line in moves:
        score += game[decrypt[line]]
    return score

def main():
    input_file = "../inputs/2.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
