"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Notice: Assume the length of given string will not exceed 1010.
"""


class Solution:
    """
    @param: s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = True
            else:
                del dic[c]

        if dic:
            return len(s) - len(dic) + 1
        else:
            return len(s)


sol = Solution()
ans = sol.longestPalindrome(s="abccccdd")
print(ans)