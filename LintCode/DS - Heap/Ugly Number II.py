"""
Ugly number is a number that only have factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Example
If n=9, return 10.

Challenge
O(n log n) or O(n) time.
"""

import heapq


class Solution_v1:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    """ Time Complexity: O(n) """

    def nthUglyNumber(self, n):
        # write your code here
        uglys = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            last_number = uglys[i - 1]
            while uglys[p2] * 2 <= last_number:
                p2 += 1
            while uglys[p3] * 3 <= last_number:
                p3 += 1
            while uglys[p5] * 5 <= last_number:
                p5 += 1

            uglys.append(min(uglys[p2] * 2, uglys[p3] * 3, uglys[p5] * 5))

        return uglys[n - 1]


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    """ Time Complexity: O(nlogn) """

    def nthUglyNumber(self, n):
        # write your code here
        visited = set()
        heap = [1]

        keys = [2, 3, 5]
        for index, value in enumerate(keys):
            visited.add(value)
            heapq.heappush(heap, value)

        for i in range(n):
            ugly = heapq.heappop(heap)
            for index, value in enumerate(keys):
                if ugly * value not in visited:
                    visited.add(ugly * value)
                    heapq.heappush(heap, ugly * value)

        return ugly

