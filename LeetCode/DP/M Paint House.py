"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a
certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0
with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.
"""


"""
最值型DP
Time Complexity: O(nk^2)
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs is None or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        num_houses, num_colors = len(costs), len(costs[0])
        f = [[float('inf') for _ in range(num_colors)] for _ in range(num_houses + 1)]

        for color in range(num_colors):
            f[0][color] = 0

        for house in range(1, num_houses + 1):
            for curr in range(num_colors):
                for prev in range(num_colors):
                    if curr != prev:
                        f[house][curr] = min(f[house][curr], f[house - 1][prev] + costs[house - 1][curr])

        return min(f[num_houses][:])



