"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more
than 1.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        is_balanced, _ = self.helper(root)
        return is_balanced

    def helper(self, root):
        if root is None:
            return True, 0

        left_balanced, left_height = self.helper(root.left)
        right_balanced, right_height = self.helper(root.right)

        if not left_balanced or not right_balanced:
            return False, -1

        if abs(left_height - right_height) > 1:
            return False, -1

        return True, max(left_height, right_height) + 1


