"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

Example
For n=4, there are 2 distinct solutions.
"""


class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def __init__(self):
        self.total = 0

    def totalNQueens(self, n):
        # write your code here
        if n <= 0:
            return []

        self.dfs(n, [])

        return self.total

    def dfs(self, n, cols):
        if len(cols) == n:
            self.total += 1
            return

        for target_col in range(n):
            if not self.is_valid(cols, target_col):
                continue

            cols.append(target_col)
            self.dfs(n, cols)
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


