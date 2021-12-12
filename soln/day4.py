#!/usr/bin/env python3

"""Advent of Code 2021 Day 4."""

import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class BingoBoard:
    """Class BingoBoard."""

    def __init__(self, board, numbers):
        """Initialize."""
        if board[0] == ' ':
            self.board = board[1:]
        else:
            self.board = board

        self.create_array()
        self.turns = 0
        self.bingo_found = False
        for number in numbers:
            self.turns += 1
            self.active_number = number
            self.check_number()
            if self.bingo_found:
                break

    def create_array(self):
        """Initialize boards as a numpy array."""
        self.board_array = np.array(
            [np.array(row.split(' '))for row in self.board.split('\n')],
            dtype=object)
        for index, sub_array in enumerate(self.board_array):
            if '' in sub_array:
                sub_array_list = list(sub_array)
                sub_array_list.remove('')
                self.board_array[index] = np.array(sub_array_list)

    def check_number(self):
        """Check if your board has the number."""
        for index, sub_array in enumerate(self.board_array):
            if self.active_number in sub_array:
                sub_array = np.where(
                    sub_array == self.active_number, 'X', sub_array)
                self.board_array[index] = sub_array
                self.check_bingo()

    def check_bingo(self):
        """Check if you have a bingo."""
        for sub_array in self.board_array:
            if list(sub_array) == ['X', 'X', 'X', 'X', 'X']:
                self.bingo()
        for i in range(0, 5):
            if sub_array.size != 0:
                if [sub_array[i] for sub_array in self.board_array] == [
                        'X', 'X', 'X', 'X', 'X']:
                    self.bingo()

    def bingo(self):
        """Found bingo. Update score."""
        self.board_sum = 0
        for sub_array in self.board_array:
            for val in sub_array:
                if val != 'X':
                    self.board_sum += int(val)
        self.score = self.board_sum*int(self.active_number)
        self.bingo_found = True


def read_file(filename):
    """Take input; return numbers and boards."""
    with open(filename, 'r') as f:
        input = f.read().replace('  ', ' ')
    numbers = input.split('\n\n')[0].split(',')
    boards = input.split('\n\n')[1:]
    return numbers, boards


def main():
    """Main."""
    numbers, boards = read_file('../inputs/4.txt')
    upper_bound = 100
    lower_bound = 0
    for board in boards:
        active_board = BingoBoard(board, numbers)
        if active_board.turns <= upper_bound:
            my_board = active_board
            upper_bound = active_board.turns
        if active_board.turns >= lower_bound:
            squid_board = active_board
            lower_bound = active_board.turns

    print("Part 1:")
    print(my_board.board_array)
    print(my_board.score)
    print("Part 2:")
    print(squid_board.board_array)
    print(squid_board.score)


if __name__ == '__main__':
    main()
