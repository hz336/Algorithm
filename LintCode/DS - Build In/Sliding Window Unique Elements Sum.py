"""
Given an array and a window size that is sliding along the array, find the sum of the count of unique elements in each window.
"""

""" O(n) time complexity, O(k) space complexity """
class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """

    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        total = 0
        results = {}
        for i in range(min(k, len(nums))):
            if nums[i] in results:
                results[nums[i]] += 1
                if results[nums[i]] == 2:
                    total -= 1
            else:
                results[nums[i]] = 1
                total += 1

        final = total

        if len(nums) <= k:
            return final

        for i in range(len(nums) - k):
            if results[nums[i]] >= 2:
                results[nums[i]] -= 1
                if results[nums[i]] == 1:
                    total += 1
            else:
                del results[nums[i]]
                total -= 1

            if nums[i + k] in results:
                results[nums[i + k]] += 1
                if results[nums[i + k]] == 2:
                    total -= 1
            else:
                results[nums[i + k]] = 1
                total += 1

            final += total

        return final


