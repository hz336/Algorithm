"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            median = self.findKth(nums1, 0, nums2, 0, n // 2 + 1)
        else:
            smaller = self.findKth(nums1, 0, nums2, 0, n // 2)
            larger = self.findKth(nums1, 0, nums2, 0, n // 2 + 1)
            median = (smaller + larger) / 2

        return median

    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b + k - 1]

        if len(B) == index_b:
            return A[index_a + k - 1]

        if k == 1:
            return min(A[index_a], B[index_b])

        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else float('inf')
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else float('inf')

        if a < b:
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        else:
            return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)


