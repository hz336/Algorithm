"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
"""

"""
最知型DP
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        f = [float('-inf') for _ in range(len(nums))]
        for index, value in enumerate(nums):
            f[index] = value
            if index != 0:
                f[index] = max(f[index], f[index - 1] + value)

        return max(f)


"""
最知型DP 
Time Complexity: O(n)
Space Complexity: O(1) with space optimization 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        max_sum, cur_sum = float('-inf'), float('-inf')
        for index, value in enumerate(nums):
            if index == 0:
                max_sum = curr_sum = max(max_sum, value)
                continue

            curr_sum = max(value, curr_sum + value)
            max_sum = max(max_sum, curr_sum)

        return max_sum


"""
Follow up: 
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Answer: 
Step1. Select the middle element of the array.
So the maximum subarray may contain that middle element or not.

Step 2.1 If the maximum subarray does not contain the middle element, then we can apply the same algorithm to the the subarray to the left of the 
middle element and the subarray to the right of the middle element.

Step 2.2 If the maximum subarray does contain the middle element, then the result will be simply the maximum suffix subarray of the left subarray 
plus the maximum prefix subarray of the right subarray

Step 3 return the maximum of those three answer.

Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, start, end):
        if start >= end:
            return nums[start]

        mid = (start + end) // 2
        left_sum = self.helper(nums, start, mid)
        right_sum = self.helper(nums, mid + 1, end)
        cross_sum = self.cross_sum(nums, start, mid, end)

        return max(left_sum, cross_sum, right_sum)

    def cross_sum(self, nums, start, mid, end):
        if start >= end:
            return nums[start]

        # left prefix sum
        for i in range(mid, start - 1, -1):
            if i == mid:
                curr_sum = left_sum = nums[i]
                continue

            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)

        # right suffix sum
        for i in range(mid + 1, end + 1):
            if i == mid + 1:
                curr_sum = right_sum = nums[i]
                continue

            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)

        return left_sum + right_sum





