"""
Find the kth smallest numbers in an unsorted integer array.
"""


""" Quick Select Algorithm - O(n) time complexity """
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        # write your code here
        ans = self.quick_select(k, nums, 0, len(nums) - 1)
        return ans

    def quick_select(self, k, nums, start, end):
        left = start
        right = end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + (k - 1) <= right:
            return self.quick_select(k, nums, start, right)

        if start + (k - 1) >= left:
            return self.quick_select(k - (left - start), nums, left, end)

        return nums[right + 1]



