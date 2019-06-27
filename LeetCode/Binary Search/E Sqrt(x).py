"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid < x:
                start = mid
            else:
                end = mid

        if end * end <= x:
            return end
        else:
            return start


"""
Follow up: 
Implement double sqrt(double x) and x >= 0.
"""

class Solution_new:
    """
    @param: x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        # write your code here
        start, end = 0, x
        eps = 1e-12

        if x < 1.0:
            end = 1.0

        while end - start >= eps:
            mid = start + (end - start) / 2
            if mid * mid < x:
                start = mid
            else:
                end = mid

        return start


