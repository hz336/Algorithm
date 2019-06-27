"""
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many
possible ways the child can run up the stairs.
"""


class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            result = [1, 2, 4]
            for i in range(n - 3):
                result.append(result[-1] + result[-2] + result[-3])
            return result[-1]
