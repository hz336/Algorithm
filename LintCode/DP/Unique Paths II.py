"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution_v1:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue

                if i == 0 and j == 0:
                    f[i][j] = 1
                elif i == 0 and j > 0:
                    f[i][j] = f[i][j - 1]
                elif i > 0 and j == 0:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[m - 1][n - 1]


"""
Time Complexity: O(mn)
Space Complexity: O(2n)
"""
class Solution_v2:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for _ in range(n)] for _ in range(2)]

        now, old = 0, 1
        for i in range(m):
            now, old = old, now
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[now][j] = 0
                    continue

                if i == 0 and j == 0:
                    f[now][j] = 1
                elif i == 0 and j > 0:
                    f[now][j] = f[now][j - 1]
                elif i > 0 and j == 0:
                    f[now][j] = f[old][j]
                else:
                    f[now][j] = f[old][j] + f[now][j - 1]

        return f[now][n - 1]


"""
Time Complexity: O(mn)
Space Complexity: O(n)
"""
class Solution_v3:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                    continue

                if i == 0 and j == 0:
                    f[j] = 1
                elif i == 0 and j > 0:
                    f[j] = f[j - 1]
                elif i > 0 and j == 0:
                    f[j] = f[j]
                else:
                    f[j] = f[j] + f[j - 1]

        return f[n - 1]
