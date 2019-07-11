"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


"""
Time Complexity: O(n^2) 
Space Complexity: O(n)
"""
class Solution:
    def minCut(self, s: str) -> int:
        if s is None or len(s) == 0:
            return False

        palin = self.cal_palin(s)

        n = len(s)
        f = [float('inf')] * (n + 1)
        f[0] = 0
        for curr in range(1, n + 1):
            for prev in range(curr):
                if palin[prev][curr - 1]:
                    f[curr] = min(f[curr], f[prev] + 1)

        return f[n] - 1

    def cal_palin(self, s):
        n = len(s)
        palin = [[False for _ in range(n)] for _ in range(n)]
        for mid in range(n):
            # odd
            start = end = mid
            while start >= 0 and end < n and s[start] == s[end]:
                palin[start][end] = True
                start -= 1
                end += 1

            # even
            start, end = mid, mid + 1
            while start >= 0 and end < n and s[start] == s[end]:
                palin[start][end] = True
                start -= 1
                end += 1

        return palin


"""
Time Complexity: O(n^3) -> Time Limit Exceeded
Space Complexity: O(n)
"""
class Solution:
    def minCut(self, s: str) -> int:
        if s is None or len(s) == 0:
            return False

        n = len(s)
        f = [float('inf')] * (n + 1)
        f[0] = 0
        for curr in range(1, n + 1):
            for prev in range(curr):
                if self.isPalin(s[prev: curr]):
                    f[curr] = min(f[curr], f[prev] + 1)

        return f[n] - 1

    def isPalin(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True



