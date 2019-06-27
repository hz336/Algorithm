"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
"""


class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """

    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

