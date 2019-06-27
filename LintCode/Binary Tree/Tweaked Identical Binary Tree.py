"""
Check two given binary trees are identical or not. Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one
node in the tree.

Notice
There is no two nodes with the same value in the tree.

Example
    1             1
   / \           / \
  2   3   and   3   2
 /                   \
4                     4
are identical.

    1             1
   / \           / \
  2   3   and   3   2
 /             /
4             4
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
    @return: true if they are tweaked identical, or false.
    """

    def isTweakedIdentical(self, a, b):
        # write your code here
        if a is None and b is None:
            return True

        if a is None and b is not None:
            return False

        if a is not None and b is None:
            return False

        if a.val != b.val:
            return False

        return self.isTweakedIdentical(a.right, b.right) and self.isTweakedIdentical(a.left, b.left) or \
               self.isTweakedIdentical(a.right, b.left) and self.isTweakedIdentical(a.left, b.right)


