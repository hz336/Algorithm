"""
Given a 2D grid, each cell is either an house 1 or empty 0 (the number zero, one), find the place to build a post office, the distance that post
office to all the house sum is smallest. Return the smallest distance. Return -1 if it is not possible.

Notice
You can pass through house and empty.
You only build post office on an empty.

Example
Given a grid:

0 1 0 0
1 0 1 1
0 1 0 0
return 6. (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)
"""


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m = len(grid)
        n = len(grid[0])
        count = 0
        rows, cols = [], []
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    count += 1
                    rows.append(x)
                    cols.append(y)

        rows.sort()
        cols.sort()

        presum_rows = [0]
        presum_cols = [0]
        for i in range(count):
            presum_rows.append(presum_rows[-1] + rows[i])
            presum_cols.append(presum_cols[-1] + cols[i])

        dist_min = math.inf
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    dist_x = self.get_dist(x, rows, presum_rows)
                    dist_y = self.get_dist(y, cols, presum_cols)
                    dist_min = min(dist_min, dist_x + dist_y)

        return dist_min

    def get_dist(self, x, array, presum):
        index = self.find_index(x, array)
        dist_index_pre = x * index - presum[index]
        dist_index_post = presum[-1] - presum[index] - (len(array) - index) * x
        dist_total = dist_index_pre + dist_index_post

        return dist_total

    def find_index(self, target, array):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] == target:
                end = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid

        if array[start] >= target:
            return start

        if array[end] >= target:
            return end

        return end + 1


