"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0
with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Example
Given n = 3, k = 3, costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is color 2, house 1 is color 3, house 2 is color 2, 2 + 5 + 3 = 10

Challenge
Could you solve it in O(nk)?
"""

import math


"""
Time Complexity: O(nk^2) -> O(nk)
"""
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):
        # write your code here
        if costs is None or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        num_houses = len(costs)
        num_colors = len(costs[0])
        f = [[0 for _ in range(num_colors)] for _ in range(num_houses + 1)]

        for house in range(num_houses):
            num_min = num_sec = -1
            for prev_color in range(num_colors):
                if num_min == -1 or f[house][prev_color] < f[house][num_min]:
                    num_sec = num_min
                    num_min = prev_color
                elif num_sec == -1 or f[house][prev_color] < f[house][num_sec]:
                    num_sec = prev_color

            for curr_color in range(num_colors):
                if curr_color != num_min:
                    f[house + 1][curr_color] = f[house][num_min] + costs[house][curr_color]
                else:
                    f[house + 1][curr_color] = f[house][num_sec] + costs[house][curr_color]

        return min(f[num_houses][:])


"""
Print optimal solution
"""
class Solution_with_path:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):
        # write your code here
        if costs is None or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        num_houses = len(costs)
        num_colors = len(costs[0])
        f = [[0 for _ in range(num_colors)] for _ in range(num_houses + 1)]
        pi = [[0 for _ in range(num_colors)] for _ in range(num_houses + 1)]

        for house in range(num_houses):
            num_min = num_sec = -1
            for prev_color in range(num_colors):
                if num_min == -1 or f[house][prev_color] < f[house][num_min]:
                    num_sec = num_min
                    num_min = prev_color
                elif num_sec == -1 or f[house][prev_color] < f[house][num_sec]:
                    num_sec = prev_color

            for curr_color in range(num_colors):
                if curr_color != num_min:
                    f[house + 1][curr_color] = f[house][num_min] + costs[house][curr_color]
                    pi[house + 1][curr_color] = num_min
                else:
                    f[house + 1][curr_color] = f[house][num_sec] + costs[house][curr_color]
                    pi[house + 1][curr_color] = num_sec

        # Find the color for the last house
        result = math.inf
        for color in range(num_colors):
            result = min(result, f[num_houses][color])
            if result == f[num_houses][color]:
                last_color = color

        # Based on the last color of the house, find the color of previous house
        color_path = [None] * num_houses
        for i in range(num_houses, 0, -1):
            color_path[i - 1] = last_color
            last_color = pi[i][last_color]

        print(color_path)

        return result


costs = [[14,2,11],[11,14,5],[14,3,10]]
sol = Solution_with_path()
ans = sol.minCostII(costs)

print(ans)
