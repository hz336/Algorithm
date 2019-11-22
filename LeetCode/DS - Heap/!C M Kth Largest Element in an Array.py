"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""

"""
Best Answer: Quick Select
Average Time Complexity: O(n)
Worst Time Complexity: O(n^2)
Space Complexity: O(1)

Disadvantage: It's an off-line algo, which cann't deal with streaming data.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = self.quick_select(nums, 0, len(nums) - 1, k)
        return ans

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1

            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quick_select(nums, start, right, k)

        if start + k - 1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))

        return nums[right + 1]


"""
Priority Queue - build-in function nlargest
Time Complexity: O(nlogk)
Space Complexity: O(k)
"""
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]



"""
Follow up: Streaming data
Time Complexity: O(nlogk)
Space Complexity: O(k)
"""
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)















