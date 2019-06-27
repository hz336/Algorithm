"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
"""


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        results = []
        if nums is None or len(nums) == 0:
            self.add_range(lower, upper, results)
            return results

        self.add_range(lower, nums[0] - 1, results)

        for i in range(len(nums) - 1):
            self.add_range(nums[i] + 1, nums[i + 1] - 1, results)

        self.add_range(nums[-1] + 1, upper, results)

        return results

    def add_range(self, start, end, results):
        if start > end:
            return
        elif start == end:
            results.append(str(start))
        else:
            results.append(str(start) + '->' + str(end))


