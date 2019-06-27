"""
Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.
"""

""" Quick Select Algorithm - O(n) time complexity """
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        ans = self.quick_select(k, A, 0, len(A) - 1)
        return ans

    def quick_select(self, k, A, start, end):
        left = start
        right = end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] > pivot:
                left += 1

            while left <= right and A[right] < pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        if start + (k - 1) <= right:
            return self.quick_select(k, A, start, right)

        if start + (k - 1) >= left:
            return self.quick_select(k - (left - start), A, left, end)

        return A[right + 1]

