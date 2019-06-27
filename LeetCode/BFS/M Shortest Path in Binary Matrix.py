"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.



Example 1:

Input: [[0,1],[1,0]]
Output: 2
Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""


from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1

        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque([(0, 0)])
        dirs = {(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)}

        steps = 1
        while queue:
            len_q = len(queue)
            for _ in range(len_q):
                x, y = queue.popleft()
                visited[x][y] = True
                for x_delta, y_delta in dirs:
                    new_x = x + x_delta
                    new_y = y + y_delta
                    if self.is_valid(grid, new_x, new_y, visited):
                        if new_x == m - 1 and new_y == n - 1:
                            return steps + 1

                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True

            steps += 1

        return -1

    def is_valid(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        return 0 <= x < m and 0 <= y < n and grid[x][y] != 1 and not visited[x][y]



