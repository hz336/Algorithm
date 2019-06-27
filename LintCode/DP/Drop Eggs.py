"""
There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.

You're given two eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.
"""

class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """

    def dropEggs(self, n):
        # write your code here
        x = 1
        while x * (x + 1) // 2 <= n:
            x += 1

        return x


sol = Solution()
ans = sol.dropEggs(n=100)
print(ans)