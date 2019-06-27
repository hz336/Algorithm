"""
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the
same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Notice
You couldn't cut wood into float length.
If you couldn't get >= k pieces, return 0.

Example
For L=[232, 124, 456], k=7, return 114.
"""

""" O(n log(longest length of the wood)) """
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if L is None or len(L) == 0:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            pieces = self.count(L, mid)
            if pieces >= k:
                start = mid
            else:
                end = mid

        if self.count(L, end) >= k:
            return end

        if self.count(L, start) >= k:
            return start

        return 0

    def count(self, L, mid):
        total = 0
        for i in range(len(L)):
            total += L[i] // mid

        return total
