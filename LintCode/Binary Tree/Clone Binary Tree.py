"""
For the given binary tree, return a deep copy of it.

Have you met this question in a real interview?
Example
Given a binary tree:

     1
   /  \
  2    3
 / \
4   5
return the new binary tree with same structure and same value:

     1
   /  \
  2    3
 / \
4   5
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
    @param root: The root of binary tree
    @return: root of new tree
    """

    def cloneTree(self, root):
        # write your code here
        self.dfs(root)
        return root

    def dfs(self, root):
        if root is None:
            return

        root_new = TreeNode(root.val)
        root_new.left = self.dfs(root.left)
        root_new.right = self.dfs(root.right)

        return root_new