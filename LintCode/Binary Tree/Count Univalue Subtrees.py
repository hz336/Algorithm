"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Have you met this question in a real interview?
Example
Given root = {5,1,5,5,5,#,5}, return 4.

              5
             / \
            1   5
           / \   \
          5   5   5
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
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """

    def __init__(self):
        self.num = 0

    def countUnivalSubtrees(self, root):
        # write your code here
        self.dfs(root)
        return self.num

    def dfs(self, root):
        if root is None:
            return True

        left_single = self.dfs(root.left)
        right_single = self.dfs(root.right)

        if not left_single or not right_single:
            return False

        if root.left and root.val != root.left.val:
            return False

        if root.right and root.val != root.right.val:
            return False

        self.num += 1

        return True