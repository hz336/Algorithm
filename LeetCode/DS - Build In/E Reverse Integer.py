"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

"""
Time Complexity: O(number of digits for the integer)
Space Complexity: O(1)
"""


class Solution:
    def reverse(self, x: 'int') -> 'int':
        rev = 0
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10

            if rev < -2 ** 31 or rev > 2 ** 31 - 1:
                return 0

        return rev * sign


