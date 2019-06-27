"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        f = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

                res = max(res, f[i][j])

        return res * res

