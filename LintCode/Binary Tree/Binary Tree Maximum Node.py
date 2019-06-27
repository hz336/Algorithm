"""
Find the maximum node in a binary tree, return the node.
"""

import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        # write your code here
        node, value = self.helper(root)
        return node

    def helper(self, root):
        if root is None:
            return None, -sys.maxsize - 1

        left_node, left_val = self.helper(root.left)
        right_node, right_val = self.helper(root.right)

        max_val = max(root.val, left_val, right_val)

        if max_val == root.val:
            return root, root.val
        elif max_val == left_val:
            return left_node, left_val
        else:
            return right_node, right_val


