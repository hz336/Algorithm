"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory

Solution
https://leetcode.com/problems/trapping-rain-water/solution/
"""


""" O(n) time and O(1) memory """
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0

        maxleft = maxright = ans = 0

        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] <= heights[r]:
                maxleft = max(maxleft, heights[l])
                ans += maxleft - heights[l]
                l += 1
            else:
                maxright = max(maxright, heights[r])
                ans += maxright - heights[r]
                r -= 1

        return ans