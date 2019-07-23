"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
"""


"""
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        x, y = m - 1, 0
        while x >= 0 and y <= n - 1:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                return True

        return False


