"""
Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.

Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5
return the node with value 3.
"""

import sys


class Solution:
    """
    @param: root: the root of binary tree
    @return: the maximum weight node
    """

    def __init__(self):
        self.node = None
        self.max_val = -sys.maxsize

    def findSubtree(self, root):
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0

        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        if left_sum + right_sum + root.val > self.max_val or self.node is None:
            self.max_val = left_sum + right_sum + root.val
            self.node = root

        return left_sum + right_sum + root.val

