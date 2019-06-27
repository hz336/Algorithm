"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# version 1. divide conquer
class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# version 2. traverse
class Solution:
    def __init__(self):
        self.num_max = 0

    def maxDepth(self, root):
        self.traverse(root, 1)
        return self.num_max

    def traverse(self, root, depth):
        if root is None:
            return

        self.num_max = max(self.num_max, depth)
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

