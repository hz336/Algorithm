"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it
upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Have you met this question in a real interview?
Example
Given a binary tree {1,2,3,4,5}

    1
   / \
  2   3
 / \
4   5
return the root of the binary tree {4,5,2,#,#,3,1}.

   4
  / \
 5   2
    / \
   3   1
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
    @param root: the root of binary tree
    @return: new root
    """

    def upsideDownBinaryTree(self, root):
        # write your code here
        root = self.dfs(root)
        return root

    def dfs(self, root):
        if root is None or root.left is None:
            return root

        root_new = self.dfs(root.left)

        root.left.left = root.right
        root.left.right = root
        root.right, root.left = None, None

        return root_new

