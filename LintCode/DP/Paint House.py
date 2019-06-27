"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a
certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0
with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Example
Given costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is blue, house 1 is green, house 2 is blue, 2 + 5 + 3 = 10
"""

import math

"""
Time Complexity: O(nk^2)
"""
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        # write your code here
        if costs is None or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        num_houses = len(costs)
        num_colors = len(costs[0])

        f = [[math.inf for _ in range(num_colors)] for _ in range(num_houses + 1)]
        for color in range(num_colors):
            f[0][color] = 0

        for house in range(1, num_houses + 1):
            for curr_color in range(num_colors):
                for prev_color in range(num_colors):
                    if curr_color != prev_color:
                        f[house][curr_color] = min(f[house][curr_color], f[house - 1][prev_color] + costs[house - 1][curr_color])

        return min(f[num_houses][:])
