"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Have you met this question in a real interview?
Example
Given the below binary tree:

  1
 / \
2   3
return 6.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import math


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        # single_path: 从root往下走到任意点的最大路径，这条路径可以不包含任何点
        # max_sum: 从树中任意到任意点的最大路径，这条路径至少包含一个点
        max_sum, single_path = self.dfs(root)
        return max_sum

    def dfs(self, root):
        if root is None:
            return -math.inf, 0

        left_sum, left_path = self.dfs(root.left)
        right_sum, right_path = self.dfs(root.right)

        max_sum = max(left_sum, right_sum, left_path + right_path + root.val)
        max_path = max(left_path + root.val, right_path + root.val, 0)

        return max_sum, max_path