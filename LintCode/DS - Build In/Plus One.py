"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example
Given [1,2,3] which represents 123, return [1,2,4].
Given [9,9,9] which represents 999, return [1,0,0,0].
"""


class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        number = 0
        for i in range(len(digits)):
            number = number * 10 + digits[i]

        number += 1

        results = []
        for c in str(number):
            results.append(int(c))

        return results

