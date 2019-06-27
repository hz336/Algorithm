"""
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

Notice
If the given node has no in-order predecessor in the tree, return null

Have you met this question in a real interview?
Example
Given root = {2,1,3}, p = 1, return null.
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
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """

    def inorderPredecessor(self, root, p):
        # write your code here
        if root is None or p is None:
            return

        predecessor = None
        while root and root.val != p.val:
            if root.val > p.val:
                root = root.left
            else:
                predecessor = root
                root = root.right

        if root is None:
            return

        if root.left is None:
            return predecessor

        root = root.left
        while root.right:
            root = root.right

        return root


