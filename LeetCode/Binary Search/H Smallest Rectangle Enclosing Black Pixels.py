"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one
black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest
(axis-aligned) rectangle that encloses all black pixels.


Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
"""

"""
Time Complexity: O(mlog(n) + nlog(m))
Space Complexity: O(1)
"""
class Solution:
    def minArea(self, image: 'List[List[str]]', x: 'int', y: 'int') -> 'int':
        if image is None or len(image) == 0 or len(image[0]) == 0:
            return -1

        m, n = len(image), len(image[0])
        left = right = y
        up = down = x

        # Find right boundary
        start, end = y, n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check_column(image, mid):
                start = mid
            else:
                end = mid

        if self.check_column(image, end):
            right = end
        elif self.check_column(image, start):
            right = start

        # Find left boundary
        start, end = 0, y
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check_column(image, mid):
                end = mid
            else:
                start = mid

        if self.check_column(image, start):
            left = start
        elif self.check_column(image, end):
            left = end

        # Find up boundary
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check_row(image, mid):
                end = mid
            else:
                start = mid

        if self.check_row(image, start):
            up = start
        elif self.check_row(image, end):
            up = end

        # Find down boundary
        start, end = x, m - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check_row(image, mid):
                start = mid
            else:
                end = mid

        if self.check_row(image, end):
            down = end
        elif self.check_row(image, start):
            down = start

        return (right - left + 1) * (down - up + 1)

    def check_column(self, image: 'List[List[str]]', col: 'int') -> 'bool':
        m, n = len(image), len(image[0])
        for i in range(m):
            if image[i][col] == '1':
                return True

        return False

    def check_row(self, image: 'List[List[str]]', row: 'int') -> 'bool':
        m, n = len(image), len(image[0])
        for j in range(n):
            if image[row][j] == '1':
                return True

        return False
