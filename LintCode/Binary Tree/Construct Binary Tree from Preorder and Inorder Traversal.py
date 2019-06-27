"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Notice
You may assume that duplicates do not exist in the tree.

Have you met this question in a real interview?
Example
Given in-order [1,2,3] and pre-order [2,1,3], return a tree:

  2
 / \
1   3
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
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

    def buildTree(self, preorder, inorder):
        # write your code here
        root = self.dfs(preorder, inorder)
        return root

    def dfs(self, preorder, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.dfs(preorder[1: root_index + 1], inorder[: root_index])
        root.right = self.dfs(preorder[root_index + 1:], inorder[root_index + 1:])

        return root


