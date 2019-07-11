"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import math


"""
Time Complexity: O(n * sqrt(n))
"""
class Solution(object):
    def numSquares(self, n):
        f = [float('inf')] * (n + 1)
        f[0] = 0
        for curr in range(1, n + 1):
            for prev in range(1, int(math.sqrt(curr)) + 1):
                f[curr] = min(f[curr], f[curr - prev * prev] + 1)

        return f[n]


