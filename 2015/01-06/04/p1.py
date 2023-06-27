#!/usr/bin/env python3

from hashlib import md5

def read_file(filename):
    with open(filename) as f:
        line = f.read()
    return line

def part1(filename):
    inkey = read_file(filename)
    res = 0
    for i in range(1000000):
        key = inkey + str(i)
        hash = md5(key.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            res = i
            break
    return res

def main():
    input_file = "in.txt"
    print("res: " + str(part1(input_file)))

if __name__ == '__main__':
    main()
