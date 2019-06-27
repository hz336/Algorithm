"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the
same character but a character may map to itself.
"""


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """

    # Version 1. dict
    def isIsomorphic1(self, s, t):
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False

        mapping = {}
        for i in range(len(s)):
            if t[i] not in mapping:
                mapping[t[i]] = s[i]
            else:
                if mapping[t[i]] != s[i]:
                    return False

        return True

    # Version 2. set(zip(t,s))
    def isIsomorphic2(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


sol = Solution()
ans = sol.isIsomorphic1(s="egg", t="ade")
print(ans)
















