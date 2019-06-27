"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Clarification
Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
"""


class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, nums):
        # write your code here
        s = set(nums)

        result = 0
        for num in nums:
            tmp = 0
            down = num - 1
            while down in s:
                tmp += 1
                s.remove(down)
                down -= 1

            up = num + 1
            while up in s:
                tmp += 1
                s.remove(up)
                up += 1

            result = max(result, up - down - 1)

        return result

