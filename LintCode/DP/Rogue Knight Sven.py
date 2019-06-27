"""
In material plane "reality", there are n + 1 planets, namely planet 0, planet 1, ..., planet n.
Each planet has a portal through which we can reach the target planet directly without passing through other planets.
But portal has two shortcomings.
First, planet i can only reach the planet whose number is greater than i, and the difference between i can not exceed the limit.
Second, it takes cost[j] gold coins to reach the planet j through the portal.
Now, Rogue Knight Sven arrives at the planet 0 with m gold coins, how many ways does he reach the planet n through the portal?

Example
Give n = 1, m = 1, limit = 1, cost = [0, 1],return 1.

Explanation:
Plan 1: planet 0 → planet 1
Give n = 1, m = 1, limit = 1, cost = [0, 2],return 0.

Explanation:
He can not reach the target planet.
Give n = 2, m = 3, limit = 2, cost = [0, 1, 1],return 2.

Explanation:
Plan 1: planet 0 → planet 1 → planet 2
Plan 2: planet 0 → planet 2
Give n = 2, m = 3, limit = 2, cost = [0, 3, 1],return 1.

Explanation:
Plan 1: planet 0 → planet 2
"""

"""
Time Complexity: O(mn^2)
Space Complexity: O(mn)
"""
class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """

    def getNumberOfWays(self, n, m, limit, cost):
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][m] = 1

        for i in range(1, n + 1):
            for j in range(m + 1):
                if j + cost[i] > m:
                    continue

                for k in range(max(0, i - limit), i):
                    f[i][j] += f[k][j + cost[i]]

        return sum(f[n][:])
