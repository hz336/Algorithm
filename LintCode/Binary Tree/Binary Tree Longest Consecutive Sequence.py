"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive
path need to be from parent to child (cannot be the reverse).

Have you met this question in a real interview?
Example
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
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

    def __init__(self):
        self.longest = 0

    def longestConsecutive(self, root):
        # write your code here
        self.dfs(root)
        return self.longest

    def dfs(self, root):
        if root is None:
            return 0

        left_max = self.dfs(root.left)
        right_max = self.dfs(root.right)

        sub_len = 1
        if root.left and root.val + 1 == root.left.val:
            sub_len = max(sub_len, left_max + 1)

        if root.right and root.val + 1 == root.right.val:
            sub_len = max(sub_len, right_max + 1)

        self.longest = max(self.longest, sub_len)

        return sub_len