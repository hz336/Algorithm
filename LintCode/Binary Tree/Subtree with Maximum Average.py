"""
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def __init__(self):
        self.max_avg = 0
        self.max_tree = None

    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.max_tree

    def helper(self, root):
        if root is None:
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        tree_sum = root.val + left_sum + right_sum
        size_tree = 1 + left_size + right_size

        if self.max_tree is None or tree_sum / size_tree > self.max_avg:
            self.max_tree = root
            self.max_avg = tree_sum / size_tree

        return tree_sum, size_tree
