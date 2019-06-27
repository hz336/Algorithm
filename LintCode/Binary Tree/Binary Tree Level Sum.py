"""
Given a binary tree and an integer which is the depth of the target level.
Calculate the sum of the nodes in the target level.

Example
Given a binary tree:

     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of the binary tree
    @param: level: the depth of the target level
    @return: An integer
    """

    def levelSum(self, root, level):
        # write your code here
        p = []
        self.helper(root, p, 1, level)
        return sum(p)

    def helper(self, root, p, index, level):
        if root is None:
            return 0

        if index == level:
            p.append(root.val)
            return

        self.helper(root.left, p, index + 1, level)
        self.helper(root.right, p, index + 1, level)



