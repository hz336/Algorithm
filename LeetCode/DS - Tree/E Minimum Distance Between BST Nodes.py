"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :
Input: root = [4,2,6,1,3,null,null]
Output: 1

Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
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

class Solution:
    def __init__(self):
        self.prev = float('-inf')
        self.ans = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node is None:
            return

        self.dfs(node.left)
        self.ans = min(self.ans, node.val - self.prev)
        self.prev = node.val
        self.dfs(node.right)
