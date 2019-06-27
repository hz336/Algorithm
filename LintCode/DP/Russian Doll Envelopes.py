"""
Description
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the
width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example
Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

import bisect

"""
Dynamic Programming + Binary Search 
Time Complexity: O(nlogn) 
"""
class Solution_v1:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here
        height = [a[1] for a in sorted(envelopes, key=lambda x: (x[0], -x[1]))]

        len_height = len(height)
        min_last = [math.inf] * (len_height + 1)
        min_last[0] = -math.inf

        for i in range(len_height):
            # find the first number in minLast >= nums[i]
            index = self.binary_search(min_last, height[i])
            min_last[index] = height[i]

        for i in range(len_height, 0, -1):
            if min_last[i] != math.inf:
                return i

        return 0

    def binary_search(self, min_last, target):
        start, end = 0, len(min_last) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if min_last[mid] < target:
                start = mid
            else:
                end = mid

        if min_last[start] >= target:
            return start
        else:
            return end


"""
Dynamic Programming + Binary Search 
Time Complexity: O(nlogn) 
"""
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here
        height = [a[1] for a in sorted(envelopes, key=lambda x: (x[0], -x[1]))]
        min_last = [0] * len(height)

        start, end = 0, 0
        for h in height:
            i = bisect.bisect_left(min_last, h, start, end)
            min_last[i] = h
            if i == end:
                end += 1

        return end


"""
Dynamic Programming
Time Complexity: O(N^2) 
"""
class Solution_v3:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here
        if envelopes is None or len(envelopes) == 0:
            return 0

        envelopes.sort(key=lambda x: (x[0], x[1]))

        n = len(envelopes)
        f = [1] * n

        for curr in range(n):
            for prev in range(curr):
                if envelopes[prev][0] < envelopes[curr][0] and envelopes[prev][1] < envelopes[curr][1]:
                    f[curr] = max(f[curr], f[prev] + 1)

        return max(f)