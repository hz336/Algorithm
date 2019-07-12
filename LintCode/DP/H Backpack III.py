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

这题从右往走是行不通的，画图可知。
先从二维数组开始，找规律，可以优化到一维数组。直接写一维，谁也做不到。
不要背诵到底是从左往右，还是从右往左。
"""
class Solution:
    def backPackIII(self, A, V, m):
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


