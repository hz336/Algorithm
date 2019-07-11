"""
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take
 the last coin wins. Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.

Example
Example 1:
Input: 1
Output: true

Example 2:
Input: 4
Output: true
Explanation:
The first player takes 1 coin at first. Then there are 3 coins left.
Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.

Challenge
O(n) time and O(1) memory
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def firstWillWin(self, n):
        if n is None or n <= 0:
            return False

        f = [None] * (n + 1)
        for i in range(1, n + 1):
            if i == 1 or i == 2:
                f[i] = True
                continue

            if f[i - 1] is False or f[i - 2] is False:
                f[i] = True
            else:
                f[i] = False

        return f[n]


"""
Time Complexity: O(n)
Space Complexity: O(1) 滚动数组
"""
class Solution:
    def firstWillWin(self, n):
        dp = [False] * 3
        dp[1] = True
        dp[2] = True

        for i in range(3, n + 1):
            dp[i % 3] = not dp[(i - 1) % 3] or not dp[(i - 2) % 3]

        return dp[n % 3]


"""
可以证明, 当硬币数目是3的倍数的时候, 先手玩家必败, 否则他必胜.
当硬币数目是3的倍数时, 每一轮先手者拿a个, 后手者拿3-a个即可, 后手必胜.
若不是3的倍数, 先手者可以拿1或2个, 此时剩余硬币个数就变成了3的倍数.

Time Complexity: O(1)
Space Complexity: O(1)
"""
class Solution:
    def firstWillWin(self, n):
        if n % 3 == 0:
            return False

        return True
