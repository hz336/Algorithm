"""
Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.
"""

from collections import defaultdict


class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        # write your code here
        n = len(A)
        m = len(A[0])
        k = len(B[0])

        mapA = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    mapA[i].append(j)

        mapB = defaultdict(list)
        for i in range(m):
            for j in range(k):
                if B[i][j] != 0:
                    mapB[i].append(j)

        C = [[0 for _ in range(k)] for _ in range(n)]

        for i in range(n):
            for j in mapA[i]:
                for l in mapB[j]:
                    C[i][l] += A[i][j] * B[j][l]

        return C

