"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3

Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 13

Output: false
"""

"""
Time Complexity: O(log(mn))
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] <= target:
                start = mid
            else:
                end = mid

        x, y = start // n, start % n
        if matrix[x][y] == target:
            return True

        x, y = end // n, end % n
        if matrix[x][y] == target:
            return True

        return False


maxtrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

target = 3

sol = Solution()
ans = sol.searchMatrix(maxtrix, target)
print(ans)


