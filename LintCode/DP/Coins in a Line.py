"""
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take
the last coin wins.

Could you please decide the first play will win or lose?

Example
n = 1, return true.

n = 2, return true.

n = 3, return false.

n = 4, return true.

n = 5, return true.

Challenge
O(n) time and O(1) memory
"""


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n is None or n <= 0:
            return False

        f = [None] * (n + 1)
        f[0] = False
        for i in range(1, n + 1):
            if i == 1 or i == 2:
                f[i] = True
            else:
                if f[i - 1] and f[i - 2]:
                    f[i] = False
                else:
                    f[i] = True

        return f[-1]