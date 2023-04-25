#!/usr/bin/python3
""" Solve N Queens problem """

import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if (n < 4):
    print("N must be at least 4")
    sys.exit(1)


def n_queens(num):
    """ prints every possible solution """
    result = []

    col = set()     # tracking the columns
    neg_diagonal = set()    # (r - 1) tracking the negative diagonals
    pos_diagonal = set()    # (r + 1)tracking the positive diagonals

    board = [[] for num in range(num)]  # empty board

    def backtracking(r):
        """recursive function for backtracking """
        if r == num:    # getting to the last row
            copy = board.copy()     # copy the current board
            result.append(copy)
            return

        for c in range(num):    # validating used columns and diagonals
            if c in col or (r - c) in neg_diagonal or (r + c) in pos_diagonal:
                continue

            # record found colums and diagonals
            col.add(c)
            neg_diagonal.add(r - c)
            pos_diagonal.add(r + c)
            board[r] = [r, c]

            # move to next row
            backtracking(r + 1)

            # undo movements
            col.remove(c)
            neg_diagonal.remove(r - c)
            pos_diagonal.remove(r + c)

            board[r] = []

    backtracking(0)
    return result


if __name__ == '__main__':
    boards = n_queens(n)
    for board in boards:
        print(board)
