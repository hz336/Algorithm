"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return 2147483647

Example
Given dividend = 100 and divisor = 9, return 11.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX

        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                print("shift: %s, b: %s, b << shift: %s" % (shift, b, b << shift))

                a -= b << shift
                ans += 1 << shift

                print("a: %s, ans: %s" % (a, ans))
            shift -= 1

        if neg:
            ans = - ans

        if ans > INT_MAX:
            return INT_MAX

        return ans


sol = Solution()
ans = sol.divide(100, 9)
print(ans)