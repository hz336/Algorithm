"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:
    def __init__(self):
        self.count = 0

    def totalNQueens(self, n: int) -> int:
        if n <= 0:
            return 0

        subset = []
        self.dfs(n, subset)
        return self.count

    def dfs(self, n, subset):
        if len(subset) == n:
            self.count += 1

        for target_col in range(n):
            if self.is_valid(target_col, subset):
                subset.append(target_col)
                self.dfs(n, subset)
                subset.pop()

    def is_valid(self, target_col, subset):
        target_row = len(subset)

        for row, col in enumerate(subset):
            if col == target_col:
                return False

            if target_row + target_col == row + col:
                return False

            if target_row - row == target_col - col:
                return False

        return True
