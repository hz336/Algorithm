"""
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.

Notice
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combination.

Example
Given n = 8
return [[2,2,2],[2,4]]
// 8 = 2 x 2 x 2 = 2 x 4.

Given n = 1
return []

Given n = 12
return [[2,6],[2,2,3],[3,4]]
"""

import math


class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        # write your code here
        results = []
        self.dfs(n, 2, [], results)

        return results

    def dfs(self, n, start, subset, results):
        if n == 1:
            if len(subset) > 1:
                results.append(subset[:])
            return

        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                subset.append(i)
                self.dfs(n // i, i, subset, results)
                subset.pop()

        subset.append(n)
        self.dfs(1, n, subset, results)
        subset.pop()
