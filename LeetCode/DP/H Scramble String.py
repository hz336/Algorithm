"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""


"""
Time Complexity: O(n^4)
Space Complexity: O(n^3)
"""
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    def isScramble(self, s1, s2):
        # write your code here
        if s1 is None or s2 is None:
            return False

        n = len(s1)
        m = len(s2)
        if n != m:
            return False

        f = [[[False for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    f[i][j][1] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    f[i][j][length] = False

                    for w in range(1, length):
                        if f[i][j][w] and f[i + w][j + w][length - w]:
                            f[i][j][length] = True
                            break

                        if f[i][j + length - w][w] and f[i + w][j][length - w]:
                            f[i][j][length] = True
                            break

        return f[0][0][n]












