"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n <= 2:
            return n

        result = [1, 2]
        for i in range(n - 2):
            result.append(result[-2] + result[-1])

        return result[-1]


sol = Solution()
ans = sol.climbStairs(n=10)
print(ans)
