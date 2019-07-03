"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

"""
Time Complexity: O(mkn)
Space Complexity: O(mn)
"""


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B or len(A) == 0 or len(B) == 0:
            return -1

        if len(A[0]) != len(B):
            return -1

        m, k, n = len(A), len(A[0]), len(B[0])
        results = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for c in range(k):
                if A[i][c] == 0:
                    continue

                for j in range(n):
                    results[i][j] += A[i][c] * B[c][j]

        return results



"""
Follow up:
It should be a data structure design problem.
You should give a reasonable data structure to present sparse matrix and multiplication method.

One potential advantage of having two hash tables is that it can be used as a sparse matrix representation. The the code becomes more reusable and 
extensible.

Time Complexity: O(mkn)
Space Complexity: O(mn)
"""


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B or len(A) == 0 or len(B) == 0:
            return -1

        m, k, n = len(A), len(A[0]), len(B[0])

        table_A, table_B = {}, {}
        for i, row in enumerate(A):
            for j, e in enumerate(row):
                if e:
                    if i not in table_A:
                        table_A[i] = {}
                    table_A[i][j] = e

        for i, row in enumerate(B):
            for j, e in enumerate(row):
                if e:
                    if i not in table_B:
                        table_B[i] = {}
                    table_B[i][j] = e

        results = [[0 for _ in range(n)] for i in range(m)]
        for i in table_A:
            for k in table_A[i]:
                if k not in table_B:
                    continue

                for j in table_B[k]:
                    results[i][j] += table_A[i][k] * table_B[k][j]

        return results






















