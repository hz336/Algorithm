"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

"""
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
    - Answer: Two pointers. O(size of nums1 + size of nums2)

What if nums1's size is small compared to num2's size? Which algorithm is better?
    - Answer: Hash set. Put nums1 to hash set, and traverse nums2

What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    - Answer: Hash set. Put nums1 to hash set, and traverse nums2 by chunks
"""


class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    # version 1. hash set
    def intersection(self, nums1, nums2):
        nums1_dict = {}
        for c in nums1:
            if c not in nums1_dict:
                nums1_dict[c] = 1
            else:
                nums1_dict[c] += 1

        results = []
        for c in nums2:
            if c in nums1_dict and nums1_dict[c] > 0:
                results.append(c)
                nums1_dict[c] -= 1

        return results
