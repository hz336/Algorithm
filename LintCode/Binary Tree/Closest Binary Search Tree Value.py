"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Notice
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Example
Given root = {1}, target = 4.428571, return 1.
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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return 0

        lower_node = self.lower_bound(root, target)
        upper_node = self.upper_bound(root, target)

        if lower_node is None:
            return upper_node.val

        if upper_node is None:
            return lower_node.val

        if target - lower_node.val > upper_node.val - target:
            return upper_node.val

        return lower_node.val

    # find the node with the largest value that's smaller than target
    def lower_bound(self, root, target):
        if root is None:
            return

        if target <= root.val:
            return self.lower_bound(root.left, target)

        # target > root.val
        lower_node = self.lower_bound(root.right, target)
        if lower_node:
            return lower_node

        return root

    # find the node with the smallest value that's larger than or equal to target
    def upper_bound(self, root, target):
        if root is None:
            return

        if target > root.val:
            return self.upper_bound(root.right, target)

        # target <= root.val
        upper_node = self.upper_bound(root.left, target)
        if upper_node:
            return upper_node

        return root

