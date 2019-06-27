"""
Find K-th largest element in an array. and N is much larger than k.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.
"""

import heapq


class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """

    def kthLargestElement2(self, nums, k):
        # write your code here
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


class Solution_v2:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """

    def kthLargestElement2(self, nums, k):
        # write your code here
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]




