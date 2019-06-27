"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        i, left, right = 0, 0, len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1


"""
Follow up: 
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors
in the order 1, 2, ... k.

Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
"""


"""
Time Complexity: O(nlogk)
Space Complexity: O(1)
"""
class Solution:
    def sortColors2(self, colors, k):
        self.rainbow_sort(colors, 0, len(colors) - 1, 1, k)
        return colors

    def rainbow_sort(self, colors, start, end, color_start, color_end):
        if start >= end:
            return

        if color_start >= color_end:
            return

        color_mid = (color_start + color_end) // 2
        left, right = start, end
        while left <= right:
            while left <= right and colors[left] <= color_mid: # colors_mid should be strictly on the left side
                left += 1

            while left <= right and colors[right] > color_mid:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbow_sort(colors, start, right, color_start, color_mid)
        self.rainbow_sort(colors, left, end, color_mid + 1, color_end)
