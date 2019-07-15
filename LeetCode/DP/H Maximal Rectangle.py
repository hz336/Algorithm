"""
Given a 2D boolean matrix filled with False and True, find the largest rectangle containing all True and return its area.

Example
Given a matrix:

[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
return 6.
"""


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    left = [[0 for _ in range(n)] for _ in range(m)]
    right = [[0 for _ in range(n)] for _ in range(m)]
    up = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        # calculate up
        for j in range(n):
            if matrix[i][j] == "0":
                up[i][j] = 0
            else:
                up[i][j] = 1
                if i > 0:
                    up[i][j] += up[i - 1][j]

        # calculate left
        l = 0
        for j in range(n):
            if matrix[i][j] == "0":
                l = left[i][j] = 0
            else:
                l += 1
                left[i][j] = l
                if i > 0 and matrix[i - 1][j] == "1":
                    left[i][j] = min(left[i][j], left[i - 1][j])

        # calculate right
        r = 0
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == "0":
                r = right[i][j] = 0
            else:
                r += 1
                right[i][j] = r
                if i > 0 and matrix[i - 1][j] == "1":
                    right[i][j] = min(right[i][j], right[i - 1][j])

    """
    For each i,j, compute the tallest rectangle containing (i, j) and up to row i while making it as wide as possible.
    The key point is that the global maximal rectangle must be such a tallest rectangle somewhere at (i, j)
    """
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, up[i][j] * (left[i][j] + right[i][j] - 1))

    return res


