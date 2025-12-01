#!/usr/bin/env python3

"""Advent of Code 2022 Day 8."""

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_parameters(grid):
    height = len(grid)
    width = len(grid[0])
    row_count = height - 1
    column_count = width - 1
    return height, width, row_count, column_count  

def part1(filename):
    grid = read_file(filename)
    height, width, row_count, column_count = get_parameters(grid) 
    visible_count = (height * 2) + (width * 2) - 4
    for row in range(1, row_count):
        row_grid = grid[row]
        for col in range(1, column_count):
            tree = row_grid[col]
            north, south, east, west = [], [], [], []
            for i in range(row - 1, -1, -1):
                north.append(tree > grid[i][col]) 
            for i in range(row + 1, len(grid)):
                south.append(tree > grid[i][col]) 
            for t in row_grid[col + 1:]:
                east.append(tree > t)
            for t in row_grid[:col]:
                west.append(tree > t)
            if all(north) or all(south) or all(east) or all(west):
                visible_count += 1
    return visible_count

def part2(filename):
    grid = read_file(filename)
    height, width, row_count, column_count = get_parameters(grid) 
    highest_score = 0
    for row in range(1, row_count):
        row_grid = grid[row]
        for col in range(1, column_count):
            tree = row_grid[col]
            for north in range(row - 1, -1, -1):
                if grid[north][col] >= tree:
                    break
            for south in range(row + 1, height):
                if grid[south][col] >= tree:
                    break
            for east in range(col + 1, width):
                if row_grid[east] >= tree:
                    break
            for west in range(col - 1, -1, -1):
                if row_grid[west] >= tree:
                    break
            score = (row - north) * (south - row) * (east - col) * (col - west)
            if score > highest_score:
                highest_score = score 
    return highest_score

def main():
    input_file = "../input/08.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
    main()
