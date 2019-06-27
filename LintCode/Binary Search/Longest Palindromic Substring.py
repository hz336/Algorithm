"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique
longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".
"""

""" 基于中心点枚举的算法 O(n^2) """
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        ansl, ansr, maxx = 0, 1, 0
        length = len(s)
        for i in range(1, length * 2):
            if i % 2 == 1:
                left = i // 2
                right = left
            else:
                left = i // 2 - 1
                right = left + 1

            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1

            if right - left > maxx:
                print("i: %s, left: %s, right: %s" % (i, left, right))
                maxx = right - left
                ansl = left
                ansr = right

        return s[ansl: ansr + 1]


sol = Solution()
ans = sol.longestPalindrome(s="abcdzdcab")
print(ans)
