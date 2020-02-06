"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
"""

"""
Time Complexity: O(log_4(n))
Space Complexity: O(1)
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False

        while num != 1:
            if num % 4 != 0:
                return False

            num = num // 4

        return True


"""
Follow up: Could you solve it without loops/recursion?

Answer: 
(4^n - 1) % 3 == 0

proof:
(1) 4^n - 1 = (2^n + 1) * (2^n - 1)
(2) among any 3 consecutive numbers, there must be one that is a multiple of 3
among (2^n-1), (2^n), (2^n+1), one of them must be a multiple of 3, and (2^n) cannot be the one, therefore either (2^n-1) or (2^n+1) must be a 
multiple of 3, and 4^n-1 must be a multiple of 3 as well.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0


