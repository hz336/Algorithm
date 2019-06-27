"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Notice
You may assume that duplicates do not exist in the tree.

Have you met this question in a real interview?
Example
Given inorder [1,2,3] and postorder [1,3,2], return a tree:

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

    def buildTree(self, inorder, postorder):
        # write your code here
        if len(inorder) != len(postorder):
            return

        root = self.dfs(inorder, postorder)
        return root

    def dfs(self, inorder, postorder):
        if not inorder:
            return

        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.dfs(inorder[: root_index], postorder[: root_index])
        root.right = self.dfs(inorder[root_index + 1:], postorder[root_index: -1])

        return root

