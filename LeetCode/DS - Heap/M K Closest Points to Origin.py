"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
"""


"""
Quick Select
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        vectors = [(p[0] ** 2 + p[1] ** 2, p[0], p[1]) for p in points]
        self.quick_select_with_target(vectors, 0, len(vectors) - 1, K)

        return [[x, y] for _, x, y in vectors[:K]]

    def quick_select_with_target(self, vectors, start, end, target):
        if start >= end:
            return start

        left, right = start, end
        pivot = vectors[(start + end) // 2]
        while left <= right:
            while left <= right and vectors[left] < pivot:
                left += 1

            while left <= right and vectors[right] > pivot:
                right -= 1

            if left <= right:
                vectors[left], vectors[right] = vectors[right], vectors[left]
                left += 1
                right -= 1

        if target - 1 <= right:
            return self.quick_select_with_target(vectors, start, right, target)

        if target - 1 >= left:
            return self.quick_select_with_target(vectors, left, end, target)

        return target


"""
Priority Queue
Time Complexity: O(nlogk)
Space Complexity: O(k)
"""
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = self.dist(point, [0, 0])
            heapq.heappush(heap, [-distance, point[0], point[1]])

            if len(heap) > K:
                heapq.heappop(heap)

        heap.sort(key=lambda x: (-x[0], x[1], x[2]))

        return [[x, y] for _, x, y in heap]

    def dist(self, a, b):
        if a is None or b is None:
            return float('-inf')

        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2




