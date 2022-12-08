#!/usr/bin/env python3

"""Advent of Code 2022 Day 7."""

def read_file(filename):
    with open(filename) as f:
        terminal = f.read().splitlines()
    return terminal

def get_sizes(filename):
    terminal = read_file(filename)
    sizes = {}
    path = []
    for line in terminal:
        cmd = line.split()
        # store absolute paths
        if cmd[0] == "$":
           if cmd[1] == "cd":
               if cmd[2] == "..":
                   path = path[:-1]
               elif cmd[2] == "/":
                   path = ["/"]
               else:
                   path.append(cmd[2])
        else:
            # get sizes of dirs
            if cmd[0] != "dir":
                currPath = ""
                for folder in path:
                    if currPath != "/" and folder != "/":
                        currPath += "/"
                    currPath += folder
                    sizes[currPath] = sizes.get(currPath, 0) + int(cmd[0])
    return sizes

def part1(filename):
    sizes = get_sizes(filename)
    res = 0
    for value in sizes.values():
        if value < 100000:
            res += value
    return res

def part2(filename):
    sizes = get_sizes(filename) 
    res = []
    disk = 70000000
    unused = 30000000 
    neededSpace = unused - (disk - sizes.get("/"))
    for value in sizes.values():
        if value >= neededSpace:
            res.append(value)
    return min(res)

def main():
    inputFile = "../inputs/7.txt"
    print(part1(inputFile))
    print(part2(inputFile))

if __name__ == '__main__':
    main()
