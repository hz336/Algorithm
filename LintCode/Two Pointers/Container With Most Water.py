"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most
water.

Solution
https://leetcode.com/problems/container-with-most-water/solution/
"""


""" O(n) time and O(1) memory """
class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """

    def maxArea(self, heights):
        # write your code here
        if heights is None or len(heights) == 0:
            return 0

        ans = 0
        left, right = 0, len(heights) - 1
        while left < right:
            if heights[left] <= heights[right]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[right] * (right - left)
                right -= 1

            ans = max(ans, area)

        return ans

