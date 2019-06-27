"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


"""
Time Complexity: O(m + n)
Space Complexity: O(1)
"""


class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return

        left, right = m - 1, n - 1
        index = m + n - 1
        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[index] = nums1[left]
                left -= 1
            else:
                nums1[index] = nums2[right]
                right -= 1

            index -= 1

        while left >= 0:
            nums1[index] = nums1[left]
            left -= 1
            index -= 1

        while right >= 0:
            nums1[index] = nums2[right]
            right -= 1
            index -= 1
