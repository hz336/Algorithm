"""
Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

Example
    1             1
   / \           / \
  2   2   and   2   2
 /             /
4             4
are identical.

    1             1
   / \           / \
  2   3   and   2   3
 /               \
4                 4
are not identical.
"""


class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None


class Solution:
    """
    @param: a: the root of binary tree a.
    @param: b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # write your code here
        if a is None and b is None:
            return True

        if a is None and b is not None:
            return False

        if a is not None and b is None:
            return False

        if a.val != b.val:
            return False

        return self.isIdentical(a.right, b.right) and self.isIdentical(a.left, b.left)
