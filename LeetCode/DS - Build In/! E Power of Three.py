"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

"""
Time Complexity: O(log_3(n))
Space Complexity: O(1)
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 3 != 0:
                return False

            n = n // 3

        return True


"""
Follow up: Could you solve it without loops/recursion?

Answer: 
An important piece of information can be deduced from the function signature.
In particular, n is of type int. In Java, this means it is a 4 byte, signed integer. 
Maximum value of int = 2^32 / 2 - 1 = 2147483647, since we use 32 bits to represent the number, half of the range is used for negative numbers and 
0 is part of the positive numbers. 

Knowing the limitation of n, we can now deduce that the maximum value of n that is also a power of three is 1162261467. We calculate this as:
floor(log_3(max_int)) = 19, so 3^19 = 1162261467

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
