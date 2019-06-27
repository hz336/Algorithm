"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example
Given n = 12, return 3 because 12 = 4 + 4 + 4
Given n = 13, return 2 because 13 = 4 + 9
"""

import math

"""
Time Complexity: O(n * sqrt(n))
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        f = [math.inf] * (n + 1)
        f[0] = 0
        for curr in range(1, n + 1):
            for prev in range(1, int(math.sqrt(curr)) + 1):
                f[curr] = min(f[curr], f[curr - prev * prev] + 1)

        return f[n]
