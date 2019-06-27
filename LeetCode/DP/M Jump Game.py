"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""

"""
可行性型DP
Time Complexity: O(N^2)
Space Complexity: O(N)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f = [False] * len(nums)
        f[0] = True

        for curr in range(len(nums)):
            for prev in range(curr):
                if f[prev] and nums[prev] + prev >= curr:
                    f[curr] = True
                    break

        return f[-1]



"""
Greedy Algorithm: O(N)
"""
class Solution_v2:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False

        farthest = nums[0]
        for index, value in enumerate(nums):
            if index <= farthest < index + value:
                farthest = index + value

        return farthest >= len(nums) - 1



