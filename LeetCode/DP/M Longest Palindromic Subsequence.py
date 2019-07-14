"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        if s is None or len(s) == 0: 
            return 0
        
        if s == s[::-1]:
            return len(s)

        n = len(s)
        f = [[1 for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            if s[i - 1] == s[i]:
                f[i - 1][i] = 2 
        
        for l in range(3, n + 1): 
            for start in range(n - l + 1): 
                end = start + l - 1
                f[start][end] = max(f[start][end - 1], f[start + 1][end])
                if s[start] == s[end]: 
                    f[start][end] = max(f[start][end], f[start + 1][end - 1] + 2)
        
        return f[0][n - 1]
    
