#!/usr/bin/env python3

"""Advent of Code 2023 Day 1."""

from utils import *
import re

def part1(data):
    sum = 0

    for line in data:
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                last_digit = char

        if first_digit is not None and last_digit is not None:
            sum += int(first_digit + last_digit)

    return sum

# def part2(data):
#     sum = 0
#     valid_digits = { 'one': '1', 
#                      'two': '2', 
#                      'three': '3',
#                      'four': '4',
#                      'five': '5',
#                      'six': '6',
#                      'seven': '7',
#                      'eight': '8',
#                      'nine': '9' }
#     pattern = '('
#     pattern_r = '('

#     for num in valid_digits:
#         pattern += num + '|'
#         pattern_r += num[::-1] +'|'

#     pattern += '\\d)'
#     pattern_r += '\\d)'

#     for line in data:
#         curr = ''
#         matches = [re.findall(pattern, line)[0], re.findall(pattern_r, line[::-1])[0][::-1]]
        
#         for match in matches:
#             if match in valid_digits:
#                 curr += valid_digits[match]
#             else:
#                 curr += match
        
#         sum += int(curr)

#     return sum

def part2(data):
    # 55686
    def checkNumber(char):
        valid_digits = { 'one': '1', 
                     'two': '2', 
                     'three': '3',
                     'four': '4',
                     'five': '5',
                     'six': '6',
                     'seven': '7',
                     'eight': '8',
                     'nine': '9' }
        if char.isdigit():
            return True
    
    sum = 0

    for line in data:
        first_digit = None
        last_digit = None

        for char in line:
            if checkNumber(char):
                if first_digit is None:
                    first_digit = char
                last_digit = char

        if first_digit is not None and last_digit is not None:
            sum += int(first_digit + last_digit)

    return sum

def main():
    filename = "../inputs/01.txt"
    data = read_input(filename)
    # print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
