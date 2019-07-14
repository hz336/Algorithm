"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish'
in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

"""
计数型DP
Time Complexity: O(mn)
Space Complexity: O(mn)
Space Complexity could be improved to O(n) by using rolling window
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[m - 1][n - 1]


"""
计数型DP
Time Complexity: O(mn)
Space Complexity: O(n)
Space Complexity is improved to O(n) by using rolling window
"""
class Solution_v2:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[j] = 1
                else:
                    f[j] = f[j] + f[j - 1]

        return f[n - 1]


