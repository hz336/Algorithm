"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        isBST, _, _ = self.dfs(root)
        return isBST

    def dfs(self, root):
        if root is None:
            return True, float('inf'), float('-inf')

        left_isBST, left_min, left_max = self.dfs(root.left)
        right_isBST, right_min, right_max = self.dfs(root.right)

        if not left_isBST or not right_isBST:
            return False, -1, -1

        if left_max >= root.val or right_min <= root.val:
            return False, -1, -1

        return True, min(left_min, root.val), max(right_max, root.val)








