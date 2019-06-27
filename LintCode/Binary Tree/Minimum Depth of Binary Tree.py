"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0

        min_depth = self.helper(root)
        return min_depth

    def helper(self, root):
        if root is None:
            return sys.maxsize

        if root.left is None and root.right is None:
            return 1

        left_min_depth = self.helper(root.left)
        right_min_depth = self.helper(root.right)

        return min(left_min_depth, right_min_depth) + 1





