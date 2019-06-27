"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1


"""
Follow up: 
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
       
这个问题在面试中不会让实现完整程序
只需要举出能够最坏情况的数据是 [1,1,1,1... 1] 里有一个0即可。
在这种情况下是无法使用二分法的，复杂度是O(n)
因此写个for循环最坏也是O(n)，那就写个for循环就好了
如果你觉得，不是每个情况都是最坏情况，你想用二分法解决不是最坏情况的情况，那你就写一个二分吧。
反正面试考的不是你在这个题上会不会用二分法。这个题的考点是你想不想得到最坏情况。
"""














