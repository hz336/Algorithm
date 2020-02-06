"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""
class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2) * x


