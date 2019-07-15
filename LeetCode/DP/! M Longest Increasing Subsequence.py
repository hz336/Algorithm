"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

"""
Dynamic Programming
Time Complexity: O(n^2)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        length = len(nums)
        f = [1] * length
        for curr in range(length):
            for prev in range(curr):
                if nums[prev] < nums[curr]:
                    f[curr] = max(f[curr], f[prev] + 1)

        return max(f)


"""
Binary Search 
Just remember the algorithm 
Time Complexity: O(nlogn)
"""

"""
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6
We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        min_last = [float('inf')] * n

        for i in range(n):
            # find the first number in minLast >= nums[i]
            index = self.binary_search(min_last, nums[i])
            min_last[index] = nums[i]

        for i in range(n - 1, -1, -1):
            if min_last[i] != float('inf'):
                return i + 1

        return 0

    def binary_search(self, min_last, target):
        start, end = 0, len(min_last) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if min_last[mid] < target:
                start = mid
            else:
                end = mid

        if min_last[start] >= target:
            return start
        else:
            return end



