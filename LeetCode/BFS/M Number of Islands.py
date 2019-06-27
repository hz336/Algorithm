"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        count = 0
        for row in range(m):
            for col in range(n):
                if self.check(grid, row, col, visited):
                    count += 1
                    self.bfs(grid, row, col, visited)

        return count

    def check(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        return 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not visited[x][y]

    def bfs(self, grid, row, col, visited):
        x_delta = [-1, 1, 0, 0]
        y_delta = [0, 0, -1, 1]

        queue = deque([(row, col)])
        visited[row][col] = True
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                new_x = x + x_delta[i]
                new_y = y + y_delta[i]
                if self.check(grid, new_x, new_y, visited):
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True

