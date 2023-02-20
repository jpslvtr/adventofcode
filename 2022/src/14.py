#!/usr/bin/env python3

"""Advent of Code 2022 Day 14."""

def read_file(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')	
    return lines

def build_walls(data):
    walls = set()
    y_max = 0
    for wall in data:
        wall = wall.split(" -> ")
        for i in range(1, len(wall)):
            x, y = wall[i].split(",")
            x, y = int(x), int(y)
            prev_x, prev_y = wall[i - 1].split(",")
            prev_x, prev_y = int(prev_x), int(prev_y)
            if y > y_max or prev_y > y_max:
                y_max = max(y, prev_y)
            y1, y2 = min(y, prev_y), max(y, prev_y)
            x1, x2 = min(x, prev_x), max(x, prev_x)
            if x == prev_x:
                for j in range(y1, y2 + 1):
                    walls.add((x, j))
            else:
                for j in range(x1, x2 + 1):
                    walls.add((j, y))
    y_max += 2
    return walls, y_max

def simulate_sand(data, p1):
    walls, y_max = build_walls(data)
    blocks = walls.copy()
    while True:
        if not p1 and (500, 0) in blocks:
            return len(blocks) - len(walls)
        x, y = 500, 0
        while True:
            if y+1 == y_max:
                if p1:
                    return len(blocks) - len(walls)
                else:
                    blocks.add((x, y))
                    break
            if (x, y+1) not in blocks:
                y += 1
            elif (x-1, y+1) not in blocks:
                x -= 1
                y += 1
            elif (x+1, y+1) not in blocks:
                x += 1
                y += 1
            else:
                blocks.add((x, y))
                break
 
def part1(filename):
    data = read_file(filename)
    return simulate_sand(data, True) 

def part2(filename):
    data = read_file(filename)
    return simulate_sand(data, False) 

def main():
    input_file = "../inputs/14.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
	main()
