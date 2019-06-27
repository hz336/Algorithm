"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Example
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

import math


# DP: Bottom-up mehtod
# Time Complexity: O(N^2)
class Solution_v2:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
            return -1

        # tate: f[x][y] = minumum path from [0][0] to [x][y]
        n = len(triangle)
        f = [[math.inf for _ in range(n)] for _ in range(n)]

        # initialize
        for i in range(n):
            f[n - 1][i] = triangle[n - 1][i]

        # Bottom up
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] = triangle[i][j] + min(f[i + 1][j], f[i + 1][j + 1])

        # Answer
        return f[0][0]


# DP: Top-down mehtod
# Time Complexity: O(N^2)
class Solution_v1:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
            return -1

        # tate: f[x][y] = minumum path from [0][0] to [x][y]
        n = len(triangle)
        f = [[math.inf for _ in range(n)] for _ in range(n)]

        # initialize
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        # top down
        for i in range(1, n):
            for j in range(1, i):
                f[i][j] = triangle[i][j] + min(f[i - 1][j - 1], f[i - 1][j])

        # answer
        best = f[n - 1][0]
        for i in range(1, n):
            best = min(best, f[n - 1][i])

        return best


