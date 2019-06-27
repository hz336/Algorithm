"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

Example
There exist two distinct solutions to the 4-queens puzzle:

[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]
"""


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        if n <= 0:
            return []

        results = []
        self.dfs(n, results, [])

        return results

    def dfs(self, n, results, cols):
        # results store all of the chessboards
        # cols store the column indices for each row
        if len(cols) == n:
            results.append(self.draw_board(n, cols))
            return

        for target_col in range(n):
            if not self.is_valid(cols, target_col):
                continue

            cols.append(target_col)
            self.dfs(n, results, cols)
            cols.pop()

    def is_valid(self, cols, target_col):
        target_row = len(cols)
        for row in range(len(cols)):
            if cols[row] == target_col:
                return False

            if row + cols[row] == target_row + target_col:
                return False

            if row - cols[row] == target_row - target_col:
                return False

        return True

    def draw_board(self, n, cols):
        board = []
        for i in range(n):
            row = ['.'] * n
            row[cols[i]] = 'Q'
            board.append(''.join(row))

        return board

