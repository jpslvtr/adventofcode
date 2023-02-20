#!/usr/bin/env python3

"""Advent of Code 2022 Day 12."""

import networkx as nx

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def parse_grid(data):
    di_graph = nx.DiGraph()
    map_data = {}
    start, end = [], []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            map_data[(i,j)] = col 
    for k in map_data.keys():
        if map_data[k] == "S":
            start.append(k)
    start = start[0]
    for k in map_data.keys():
        if map_data[k] == "E":
            end.append(k)
    end = end[0]
    map_data[end] = "z"
    map_data[start] = "s"
    for (x, y) in map_data.keys():
        neighbor_check, neighbor_check_ord = [], []
        neighbor = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        neighbor = [p for p in neighbor if p in map_data.keys()]
        neighbor = [p for p in neighbor if (ord(map_data[p]) - ord(map_data[(x, y)])) <= 1]
        for a in neighbor:
            di_graph.add_edge((x, y), a)
    return map_data, di_graph, start, end

def part1(filename):
    data = read_file(filename)
    _, di_graph, start, end = parse_grid(data)
    shortest_path = nx.shortest_path(di_graph, start, end)
    return (len(shortest_path) - 1)  

def part2(filename):
    data = read_file(filename)
    map_data, di_graph, start, end = parse_grid(data)
    candidates = [k for k in map_data.keys() if map_data[k] == "a"]
    paths = []
    for c in candidates:
        if nx.has_path(di_graph, c, end):
            shorted_path = nx.shortest_path(di_graph, c, end)
            paths.append(len(shorted_path) - 1)
    return min(paths)

def main():
    input_file = "../inputs/12.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == '__main__':
	main()
