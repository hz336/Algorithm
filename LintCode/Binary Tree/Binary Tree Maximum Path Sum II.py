"""
Given a binary tree, find the maximum path sum from root.

The path may end at any node in the tree and contain at least one node in it.

Example
Given the below binary tree:

  1
 / \
2   3
return 4. (1->3)
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
    @param root: the root of binary tree.
    @return: An integer
    """

    def maxPathSum2(self, root):
        # write your code here
        max_sum = self.dfs(root)
        return max_sum

    def dfs(self, root):
        if root is None:
            return -math.inf

        l_max_sum = self.dfs(root.left)
        r_max_sum = self.dfs(root.right)

        max_sum = max(l_max_sum + root.val, r_max_sum + root.val, root.val)

        return max_sum

