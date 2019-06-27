"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        is_balanced, _ = self.dfs(root)
        return is_balanced

    def dfs(self, root):
        if root is None:
            return True, 0

        left_balanced, left_height = self.dfs(root.left)
        right_balanced, right_height = self.dfs(root.right)

        if not left_balanced or not right_balanced:
            return False, -1

        if abs(left_height - right_height) > 1:
            return False, -1

        return True, max(left_height, right_height) + 1

