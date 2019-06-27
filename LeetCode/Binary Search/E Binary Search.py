"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists,
then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1


sol = Solution()
ans = sol.search(nums=[1, 2, 3, 4, 5, 6], target=3)
print(ans)
