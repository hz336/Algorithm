"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
"""


"""
Best Answer: DP / Greedy Algo
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return -1

        ugly = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            last_number = ugly[i - 1]
            while ugly[p2] * 2 <= last_number:
                p2 += 1

            while ugly[p3] * 3 <= last_number:
                p3 += 1

            while ugly[p5] * 5 <= last_number:
                p5 += 1

            next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
            ugly.append(next_ugly)

        return ugly[-1]


"""
Heap
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited = set()
        heap = [1]
        for i in [2, 3, 5]:
            visited.add(i)
            heapq.heappush(heap, i)

        # It takes O(logn) to insert an element to heap / priority queue
        for i in range(n):
            ugly = heapq.heappop(heap)
            for j in [2, 3, 5]:
                if ugly * j not in visited:
                    visited.add(ugly * j)
                    heapq.heappush(heap, ugly * j)

        return ugly


