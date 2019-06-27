"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def isPerfectSquare(self, num: 'int') -> 'bool':
        start, end = 0, num
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid <= num:
                start = mid
            else:
                end = mid

        if start * start == num:
            return True

        if end * end == num:
            return True

        return False
