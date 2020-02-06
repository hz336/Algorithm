"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        while n != 1:
            if n % 2 != 0:
                return False
            n = n // 2

        return True

"""
Follow up: Could you solve it without loops/recursion?

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


