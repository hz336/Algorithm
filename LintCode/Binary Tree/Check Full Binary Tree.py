"""
A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes. Conversely, there is no node in a full binary
tree, which has one child node. More information about full binary trees can be found here.

Full Binary Tree
      1
     / \
    2   3
   / \
  4   5

Not a Full Binary Tree
      1
     / \
    2   3
   /
  4
Have you met this question in a real interview?
Example
Given tree {1,2,3}, return true
Given tree {1,2,3,4}, return false
Given tree {1,2,3,4,5} return true
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
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        # write your code here
        is_full = self.dfs(root)
        return is_full

    def dfs(self, root):
        if root is None:
            return True

        if root.left and not root.right or root.right and not root.left:
            return False

        left_full = self.dfs(root.left)
        right_full = self.dfs(root.right)

        return left_full and right_full



