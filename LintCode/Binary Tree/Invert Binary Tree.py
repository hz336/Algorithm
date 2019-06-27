"""
Invert a binary tree.

Example
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)

    def dfs(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left

        if root.left:
            self.dfs(root.left)

        if root.right:
            self.dfs(root.right)

