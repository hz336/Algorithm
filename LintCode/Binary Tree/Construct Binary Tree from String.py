"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's
value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Notice
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
Have you met this question in a real interview?

Example
Given s = "4(2(3)(1))(6(5))", return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """

    def str2tree(self, s):
        # write your code here
        root = self.dfs(s)
        return root

    def dfs(self, s):
        if s is None or len(s) == 0:
            return

        left_start = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            left_start = 1

        val = 0
        while left_start < len(s) and s[left_start] not in ['(', ')']:
            val = val * 10 + int(s[left_start])
            left_start += 1

        root = TreeNode(val * sign)

        if left_start == len(s):
            return root

        count = 1
        left_end = left_start
        while count != 0:
            left_end += 1
            if s[left_end] == '(':
                count += 1
            elif s[left_end] == ')':
                count -= 1

        root.left = self.dfs(s[left_start + 1: left_end])

        if left_end < len(s) - 1:
            root.right = self.dfs(s[left_end + 2: len(s) - 1])

        return root











