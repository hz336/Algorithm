"""
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Example
Given [1,2,3,4], k = 2, target = 5.

There are 2 solutions: [1,4] and [2,3].

Return 2.
"""

"""
Time Complexity: O(mnk)
Space Complexity: O(mk)
"""
class Solution_v1:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    def kSum(self, A, k, target):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        n = len(A)
        f = [[0 for _ in range(target + 1)] for _ in range(k + 1)]
        f[0][0] = 1

        for i in range(1, n + 1):
            for j in range(k, -1, -1):
                for t in range(target, -1, -1):
                    if j > 0 and t >= A[i - 1]:
                        f[j][t] += f[j - 1][t - A[i - 1]]

        return f[k][target]



"""
Time Complexity: O(mnk)
Space Complexity: O(mnk)
"""
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    def kSum(self, A, k, target):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        n = len(A)
        f = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
        f[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(k + 1):
                for t in range(target + 1):
                    f[i][j][t] = f[i - 1][j][t]
                    if j > 0 and t >= A[i - 1]:
                        f[i][j][t] += f[i - 1][j - 1][t - A[i - 1]]

        return f[n][k][target]
