#!/usr/bin/env python3

"""Advent of Code 2022 Day 9."""

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def step(self, direction):
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y += 1
        else:
            self.y -= 1

    def follow(self, head):
        if abs(head.x - self.x) <= 1 and abs(head.y - self.y) <= 1:
            return
        if self.x < head.x:
            self.x += 1
        elif self.x > head.x:
            self.x -= 1
        if self.y < head.y:
            self.y += 1
        elif self.y > head.y:
            self.y -= 1

def part1(filename):
    lines = read_file(filename)
    head, tail = Knot(), Knot()
    tail_visited = set()
    for line in lines:
        direction, step = line.split()
        for _ in range(int(step)):
            head.step(direction)
            tail.follow(head)
            tail_visited.add((tail.x, tail.y))
    return len(tail_visited)

def part2(filename):
    lines = read_file(filename)
    knots = []
    for _ in range(10):
        knots.append(Knot())
    tail_visited = set()
    for line in lines:
        direction, step = line.split()
        for _ in range(int(step)):
            knots[-1].step(direction)
            for i in range(9)[::-1]:
                knots[i].follow(knots[i + 1])
            tail_visited.add((knots[0].x, knots[0].y))
    return len(tail_visited) 

def main():
    input_file = "../inputs/09.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
