#!/usr/bin/env python3

"""Advent of Code 2022 Day 11."""

import re
from functools import reduce

def read_file(filename):
	with open(filename) as f:
		 lines = f.read().strip().split('\n\n')
	return lines

def worry_level(item, operation):
    op, level = operation
    if level == 'old':
        level = item
    else:
        level = int(level)
    match op:
        case '+':
            item += level
        case '-':
            item -= level
        case '*':
            item *= level
        case '/':
            item /= level
    return int(item)

def monkey_data(inputfile):
	troop = [] # a group of monkeys = troop
	lines = read_file(inputfile)
	for monkey in lines:
		monkey = monkey.split('\n')
		items = [int(x) for x in re.findall('(\d+)', monkey[1])]
		operation = re.findall('Operation: new = old ([+\-\*/]) (\d+|old)', monkey[2])[0]
		test = int(re.findall('Test: divisible by (\d+)', monkey[3])[0])
		test_true = int(re.findall('If true: throw to monkey (\d+)', monkey[4])[0])
		test_false = int(re.findall('If false: throw to monkey (\d+)', monkey[5])[0])	
		troop.append({
			'items': items, 'operation': operation,	'test': test,
            'test_true': test_true, 'test_false': test_false, 'worry_level': 0
		})
	return troop

def part1(filename):
	troop = monkey_data(filename)
	for _ in range(20):
		for monkey in troop:
			for item in monkey['items']:
				monkey['worry_level'] += 1
				item = worry_level(item, monkey['operation'])
				item /= 3 
				item = int(item)
				if item % monkey['test'] == 0:
					troop[monkey['test_true']]['items'].append(item)
				else:
					troop[monkey['test_false']]['items'].append(item)
			monkey['items'] = []
	monkey_business = []
	for monkey in troop:
		monkey_business.append(monkey['worry_level'])
	monkey_business = sorted(monkey_business, reverse=True)
	return (monkey_business[0] * monkey_business[1])

def part2(filename):
	troop = monkey_data(filename)
	lcm = reduce((lambda x, y: x * y), [x['test'] for x in troop])
	for _ in range(10000):
		for monkey in troop:
			for item in monkey['items']:
				monkey['worry_level'] += 1
				item = worry_level(item, monkey['operation'])
				item = int(item) % lcm
				if item % monkey['test'] == 0:
					troop[monkey['test_true']]['items'].append(item)
				else:
					troop[monkey['test_false']]['items'].append(item)
			monkey['items'] = []
	monkey_business = []
	for monkey in troop:
		monkey_business.append(monkey['worry_level'])
	monkey_business = sorted(monkey_business, reverse=True)
	return (monkey_business[0] * monkey_business[1])

def main():
	input_file = "../input/11.txt"
	print(part1(input_file))
	print(part2(input_file))

if __name__ == '__main__':
	main()
