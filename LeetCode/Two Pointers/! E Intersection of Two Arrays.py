"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""

"""
Version 1: python build-in set operations
"""
class Solution_v1:
    # version 1. python build-in set
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1).intersection(set(nums2)))


"""
Version 2: hash set & traverse 
Time Complexity: O(m + n)
Space Complexity: O(min(m, n))
"""
class Solution_v2:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        results = []
        for c in nums2:
            if c in nums1:
                results.append(c)
                nums1.remove(c)

        return results

"""
Version 3: sort & binary search
Time Complexity: binary search nums1 O(nlogn) + traverse nums2 O(mlogn) = O((m + n)logn) 
Space Complexity: O(1)
"""
class Solution_v3:
    def intersection(self, nums1, nums2):
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1
        else:
            s_nums = nums1
            b_nums = nums2

        s_nums.sort()
        for num in b_nums:
            if self.binary_seach(s_nums, num):
                result.add(num)
        return list(result)

    def binary_seach(self, nums, target):
        if not nums or len(nums) == 0:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = start + (end - start) // 2

            if nums[middle] <= target:
                start = middle
            elif nums[middle] > target:
                end = middle

        if nums[end] == target or nums[start] == target:
            return True
        return False


"""
Version 4: two pointers if already sorted
Time Complexity: O(m + n)
Space Complexity: O(1)
"""
class Solution_v4:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []

        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                result.append(nums1[left])
                left += 1
                right += 1
                while left < len(nums1) and nums1[left] == nums1[left - 1]:
                    left += 1
                while right < len(nums2) and nums2[right] == nums2[right - 1]:
                    right += 1

            elif nums1[left] > nums2[right]:
                right += 1

            else:
                left += 1

        return result
