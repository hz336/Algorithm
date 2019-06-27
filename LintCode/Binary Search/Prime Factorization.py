"""
Prime factorize a given integer.

Notice
You should sort the factors in ascending order.

Example
Given 10, return [2, 5].
Given 660, return [2, 2, 3, 5, 11].
"""


class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        # write your code here
        results = []
        i = 2
        while i * i <= num:
            while num % i == 0:
                num /= i
                results.append(i)

            i += 1

        if num != 1:
            results.append(int(num))

        return results