"""
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum
of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

Notice
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)
"""

from collections import deque
import math


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    """
    对每个 house 做 BFS
    
    记录每个 empty：
        1. 能被多少个 house 触及
        2. 这些能触及的 house 到达这个 empty 的总步数之和
    
    如果最后每个 empty 都无法被所有 house 触及 (即不等于 house 个数)，则返回 -1
    如果有能被所有 house 触及的 empty，取其最小的返回
    
    Time Complexity: O(houses x rows x cols)
    """

    def shortestDistance(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return -1

        m = len(grid)
        n = len(grid[0])
        num_reachable = [[0 for _ in range(n)] for _ in range(m)]
        distance = [[0 for _ in range(n)] for _ in range(m)]

        num_house = 0
        for x in range(m):
            for y in range(n):
                if self.check(grid, x, y, 1):
                    num_house += 1
                    self.bfs(grid, distance, num_reachable, x, y)

        min_dist = math.inf
        for x in range(m):
            for y in range(n):
                if self.check(grid, x, y, 0) and num_reachable[x][y] == num_house:
                    min_dist = min(min_dist, distance[x][y])

        if min_dist != math.inf:
            return min_dist
        else:
            return -1

    def check(self, grid, x, y, name):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x < m and 0 <= y < n and grid[x][y] == name

    def bfs(self, grid, distance, num_reachable, x, y):
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        x_delta = [-1, 1, 0, 0]
        y_delta = [0, 0, -1, 1]

        queue = deque([(x, y)])
        visited[x][y] = True

        steps = 0
        while queue:
            steps += 1

            len_q = len(queue)
            for _ in range(len_q):
                x, y = queue.popleft()
                for i in range(4):
                    new_x = x + x_delta[i]
                    new_y = y + y_delta[i]
                    if self.check(grid, new_x, new_y, 0) and not visited[new_x][new_y]:
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))
                        distance[new_x][new_y] += steps
                        num_reachable[new_x][new_y] += 1

