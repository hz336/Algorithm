"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
"""

"""
最值型DP
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        f = [0] * len(nums)
        for index, value in enumerate(nums):
            if index == 0:
                f[index] = 1
            else:
                if value > nums[index - 1]:
                    f[index] = f[index - 1] + 1
                else:
                    f[index] = 1

        return max(f)


"""
最值型DP
Time Complexity: O(n)
Space Complexity: O(n)
shorter version
"""
class Solution_v2:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        f = [1] * len(nums)
        for index, value in enumerate(nums):
            if index != 0 and value > nums[index - 1]:
                f[index] = f[index - 1] + 1

        return max(f)


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution_v3:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        num_max, num_prev = 1, 1
        for index, value in enumerate(nums):
            if index != 0 and value > nums[index - 1]:
                num_max = max(num_max, num_prev + 1)
                num_prev += 1
            else:
                num_prev = 1

        return num_max




















