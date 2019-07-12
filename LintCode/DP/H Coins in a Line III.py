"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player
with the larger amount of money wins.

Could you please decide the first player will win or lose?

Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

Challenge
Follow Up Question:

If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n) time?
"""


class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        if values is None or len(values) == 0:
            return True

        # f[i][j] means when one faces A[i...j], and it's his turn, what's the
        # maximum difference between his sum and his opponent's sum, assuming
        # both sides takint the optimal strategies.
        n = len(values)
        f = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            f[i][i] = values[i]

        for l in range(2, n + 1):
            for start in range(n - l + 1):
                end = start + l - 1
                f[start][end] = max(values[start] - f[start + 1][end], values[end] - f[start][end - 1])

        return f[0][n - 1] > 0

