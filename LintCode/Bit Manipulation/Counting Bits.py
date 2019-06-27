"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and
return them as an array.

Example
Given num = 5 you should return [0,1,1,2,1,2].

Challenge
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
"""


"""
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """

    def countBits(self, num):
        # write your code here
        results = [0] * (num + 1)
        for i in range(1, num + 1):
            results[i] = i % 2 + results[i >> 1]

        return results
