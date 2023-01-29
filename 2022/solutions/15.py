#!/usr/bin/env python3

"""Advent of Code 2022 Day 15."""

import re
import time

start_time = time.time()

def read_file(filename):
    with open(filename) as f:
        lines = f.read()	
    return lines

def get_sensors(data):
    regex = r'Sensor at x=(-?[\d]+), y=(-?[\d]+): closest beacon is at x=(-?[\d]+), y=(-?[\d]+)'
    sensors = {}
    for line in data.splitlines():
        position = list(map(int, re.findall(regex, line)[0]))
        sensor = position[0], position[1]
        beacon = position[2], position[3]
        sensors[sensor] = beacon
    return sensors

def get_manhattan(sensor, beacon):
    dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    return dist

def get_occupied(sensors, target_row, part = 1, min_p = 0, max_p = float('inf')):
    range = [0, 0]
    res = []
    for sensor in sensors:
        beacon = sensors[sensor]
        dist_row = abs(sensor[1] - target_row)
        dist_beacon = get_manhattan(sensor, beacon)
        if dist_row <= dist_beacon:
            closest_y = sensor[0]
            between = dist_beacon - dist_row
            min_x = closest_y - between
            max_x = closest_y + between
            if part == 2:
                res.append([max(min_p, min_x), min(max_x, max_p)])
            if min_x < range[0]:
                range[0] = min_x
            if max_x > range[1]:
                range[1] = max_x
    return range, res

def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    for i in intervals[1:]:
        if res[-1][0] <= i[0] <= res[-1][-1]:
            res[-1][-1] = max(res[-1][-1], i[-1])
        else:
            res.append(i)
    return res

def tuning_freq(sensors, max_p):
    for i in range(max_p + 1):
        if i > 0 and i % 250_000 == 0:
            print(f'y={i}...')
        overlaps = merge(get_occupied(sensors, i, part = 2, max_p = max_p)[1])
        if len(overlaps) > 1 and overlaps[1][0] - overlaps[0][1] > 1:
            freq = i + 4000000 * (overlaps[0][1] + 1)
            return freq

def part1(filename):
    data = read_file(filename)
    sensors = get_sensors(data)
    res = sum(map(abs, get_occupied(sensors, 2000000)[0]))
    return res

def part2(filename):
    data = read_file(filename)
    sensors = get_sensors(data)
    res = tuning_freq(sensors, 4000000) 
    return res

def main():
    input_file = "../inputs/15.txt"
    print(part1(input_file))
    print(part2(input_file))
    print("--- %.2f seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()
