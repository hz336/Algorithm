"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the
width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

"""
计数型DP
Time Complexity: O(N^2) 
"""

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes is None or len(envelopes) == 0:
            return 0

        envelopes.sort()  # envelopes.sort(key=lambda: x[0], x[1])
        length = len(envelopes)
        f = [1] * length
        for curr in range(length):
            for prev in range(curr):
                if envelopes[prev][0] < envelopes[curr][0] and envelopes[prev][1] < envelopes[curr][1]:
                    f[curr] = max(f[curr], f[prev] + 1)

        return max(f)

