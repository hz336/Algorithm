"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

from collections import deque

"""
Time Complexity: O(n)
Space Complexity: O(k)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or len(nums) == 0:
            return []

        queue = deque()
        for i in range(len(nums)):
            self.clean(nums, k, queue, i)
            queue.append(i)
            if i < k - 1:
                pass
            elif i == k - 1:
                output = [nums[queue[0]]]
            else:
                output.append(nums[queue[0]])

        return output

    def clean(self, nums, k, queue, i):
        if queue and queue[0] == i - k:
            queue.popleft()

        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()







