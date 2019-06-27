"""
Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
import math


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        if not points:
            return

        heap = []
        for point in points:
            distance = self.get_distance(origin, point)
            heapq.heappush(heap, [-distance, point.x, point.y])

            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(key=lambda x: (-x[0], x[1], x[2]))

        return [[x, y] for _, x, y in heap]

    def get_distance(self, a, b):
        if a is None or b is None:
            return math.inf

        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
