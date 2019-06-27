"""
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination
position, return the length of the route. Return -1 if knight can not reached.

Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)

Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
"""

from collections import deque


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[source.x][source.y] = True

        x_delta = [1, 1, -1, -1, 2, 2, -2, -2]
        y_delta = [2, -2, 2, -2, 1, -1, 1, -1]

        steps = 0
        queue = deque([source])
        while queue:
            len_q = len(queue)
            for _ in range(len_q):
                node = queue.popleft()
                x, y = node.x, node.y

                if x == destination.x and y == destination.y:
                    return steps

                for i in range(8):
                    x_new = x + x_delta[i]
                    y_new = y + y_delta[i]
                    if self.check(x_new, y_new, grid, visited):
                        visited[x_new][y_new] = True
                        queue.append(Point(x_new, y_new))
            steps += 1

        return -1

    def check(self, x, y, grid, visited):
        m = len(grid)
        n = len(grid[0])
        if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == 0:
            return True
















