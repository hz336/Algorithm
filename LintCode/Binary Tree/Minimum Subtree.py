"""
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
"""

import math


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def __init__(self):
        self.min_tree = math.inf
        self.min_root = None

    def findSubtree(self, root):
        # write your code here
        self.dfs(root)
        return self.min_root

    # 1. 递归的定义：return root's sum
    def dfs(self, root):
        if root is None:
            return 0

        # divide conquer + merge
        sum_tree = root.val + self.dfs(root.left) + self.dfs(root.right)

        # 打擂台 (traverse)
        # compare vs global variable
        if sum_tree < self.min_tree:
            self.min_tree = sum_tree
            self.min_root = root

        return sum_tree
