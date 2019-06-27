"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:
Input: [[0,1],[1,0]]
Output: 1

Example 2:
Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""

from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([])

        # 1. DFS to find an island, mark it in visited
        found = False
        for row in range(m):
            if found is True:
                break

            for col in range(n):
                if grid[row][col]:
                    self.dfs(grid, row, col, visited, dirs, queue)
                    found = True
                    break

        # 2. BFS to expand the 1st island to reach 2nd island
        steps = self.bfs(grid, visited, dirs, queue)

        return steps

    def is_valid(self, grid, row, col, visited):
        m, n = len(grid), len(grid[0])
        return 0 <= row < m and 0 <= col < n and not visited[row][col]

    def dfs(self, grid, row, col, visited, dirs, queue):
        if not self.is_valid(grid, row, col, visited) or grid[row][col] == 0:
            return

        visited[row][col] = True
        queue.append((row, col))
        for i in range(4):
            new_row = row + dirs[i][0]
            new_col = col + dirs[i][1]
            self.dfs(grid, new_row, new_col, visited, dirs, queue)

    def bfs(self, grid, visited, dirs, queue):
        steps = 0
        while queue:
            len_q = len(queue)
            for _ in range(len_q):
                row, col = queue.popleft()
                for i in range(4):
                    new_row = row + dirs[i][0]
                    new_col = col + dirs[i][1]
                    if self.is_valid(grid, new_row, new_col, visited):
                        if grid[new_row][new_col] == 1:
                            return steps
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = True

            steps += 1

        return -1










