"""
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Notice
The Nth fibonacci number won't exceed the max value of signed 32-bit integer in the test cases.
"""


class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b

        return a
