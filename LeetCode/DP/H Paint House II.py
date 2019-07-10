"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0
with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Follow up:
Could you solve it in O(nk) runtime?
"""

"""
最值型DP
Time Complexity: O(nk^2) -> O(nk)
Space Compleixty: O(nk)
"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if costs is None or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        num_houses, num_colors = len(costs), len(costs[0])
        f = [[0 for _ in range(num_colors)] for _ in range(num_houses + 1)]

        for i in range(1, num_houses + 1):
            num_min, num_sec = -1, -1
            for prev in range(num_colors):
                if num_min == -1 or f[i - 1][prev] < f[i - 1][num_min]:
                    num_sec = num_min
                    num_min = prev
                elif num_sec == -1 or f[i - 1][prev] < f[i - 1][num_sec]:
                    num_sec = prev

            for curr in range(num_colors):
                if curr != num_min:
                    f[i][curr] = f[i - 1][num_min] + costs[i - 1][curr]
                else:
                    f[i][curr] = f[i - 1][num_sec] + costs[i - 1][curr]

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

