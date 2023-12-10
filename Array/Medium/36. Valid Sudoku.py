from typing import *


def check_col(board, i, j):
    result = board[i][j]

    for k in range(9):
        if result == board[k][j] and k != i:
            return True

    return False


def check_square(board, i, j):
    result = board[i][j]
    square = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    for sq in square:
        if i in sq:
            row_x, row_y = sq[0], sq[2]
        if j in sq:
            col_x, col_y = sq[0], sq[2]

    for k in range(row_x, row_y + 1):
        for s in range(col_x, col_y + 1):
            if result == board[k][s] and (k != i or s != j):
                return True

    return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                if cur in (board[i][:j] + board[i][j + 1:]) or check_col(board, i, j) or check_square(board, i, j):
                    return False

        return True


#Time Complexity: O(9^2)
#Space Complexity: O(9)