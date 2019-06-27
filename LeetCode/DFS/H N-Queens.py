"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []

        results = []
        subset = []
        self.dfs(n, subset, results)
        return results

    def dfs(self, n, subset, results):
        if len(subset) == n:
            results.append(self.draw(subset))

        for target_col in range(n):
            if self.is_valid(target_col, subset):
                subset.append(target_col)
                self.dfs(n, subset, results)
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

    def draw(self, subset):
        chessboard = []
        n = len(subset)
        for i in range(n):
            row = ['.'] * n
            row[subset[i]] = 'Q'
            row_str = ''.join(row)
            chessboard.append(row_str)

        return chessboard









