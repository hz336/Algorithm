"""
Given a binary tree, find the length of the longest consecutive sequence path.
The path could be start and end at any node in the tree

Have you met this question in a real interview?
Example
    1
   / \
  2   0
 /
3
Return 4 // 0-1-2-3
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
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive2(self, root):
        # write your code here
        max_len, _, _ = self.dfs(root)
        return max_len

    def dfs(self, root):
        if root is None:
            return 0, 0, 0

        left_len, left_down, left_up = self.dfs(root.left)
        right_len, right_down, right_up = self.dfs(root.right)

        down, up = 0, 0
        if root.left and root.left.val + 1 == root.val:
            down = max(down, left_down + 1)

        if root.left and root.left.val - 1 == root.val:
            up = max(up, left_up + 1)

        if root.right and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)

        if root.right and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)

        max_len = down + 1 + up
        max_len = max(max_len, left_len, right_len)

        return max_len, down, up

