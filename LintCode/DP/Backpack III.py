"""
Given n kind of items with size Ai and value Vi (each item has an infinite number available) and a backpack with size m. What's the maximum value can
you put into the backpack?

Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
"""

import math




"""
Time Complexity: O(mn)
Space complexity: O(m)
"""
class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        # write your code here
        if A is None or V is None:
            return 0

        n = len(A)
        f = [-math.inf] * (m + 1)
        f[0] = 0

        for item in range(1, n + 1):
            for weight in range(1, m + 1):
                if weight >= A[item - 1] and f[weight - A[item - 1]] != -math.inf:
                    f[weight] = max(f[weight], f[weight - A[item - 1]] + V[item - 1])

        return max(f)
