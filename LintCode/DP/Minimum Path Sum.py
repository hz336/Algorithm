"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
"""

import math

"""
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""
class Solution_v1:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        f = [[math.inf for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                    continue
                elif i == 0 and j > 0:
                    f[i][j] = f[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]

        return f[m - 1][n - 1]


"""
Time Complexity: O(m * n)
Space Complexity Optimization: O(mn) -> O(2n)
Rolling window
"""
class Solution_v2:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        f = [[math.inf for _ in range(n)] for _ in range(2)]

        old, now = 0, 1
        for i in range(m):
            old, now = now, old

            for j in range(n):
                if i == 0 and j == 0:
                    f[now][j] = grid[i][j]
                    continue
                elif i == 0 and j > 0:
                    f[now][j] = f[now][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    f[now][j] = f[old][j] + grid[i][j]
                else:
                    f[now][j] = min(f[old][j], f[now][j - 1]) + grid[i][j]

        return f[now][n - 1]


"""
Time Complexity: O(m * n)
Space Complexity: O(n)
"""
class Solution_v3:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return

        m = len(grid)
        n = len(grid[0])
        f = [math.inf for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[j] = grid[i][j]
                elif i == 0 and j > 0:
                    f[j] = f[j - 1] + grid[i][j]
                elif i > 0 and j == 0:
                    f[j] = f[j] + grid[i][j]
                else:
                    f[j] = min(f[j], f[j - 1]) + grid[i][j]

        return f[-1]


"""
Time Complexity: O(m * n)
Space Complexity: O(1)
Bad practice: Overwrite the input list
"""
class Solution_v4:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]




