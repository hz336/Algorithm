"""
It's follow up problem for Binary Tree Longest Consecutive Sequence II

Given a k-ary tree, find the length of the longest consecutive sequence path.
The path could be start and end at any node in the tree

Have you met this question in a real interview?
Example
An example of test data: k-ary tree 5<6<7<>,5<>,8<>>,4<3<>,5<>,3<>>>, denote the following structure:


     5
   /   \
  6     4
 /|\   /|\
7 5 8 3 5 3

Return 5, // 3-4-5-6-7
"""

"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        max_len, _, _ = self.dfs(root)
        return max_len

    def dfs(self, root):
        if root is None:
            return 0, 0, 0

        max_len, up, down = 0, 0, 0
        for child in root.children:
            child_len, child_up, child_down = self.dfs(child)
            max_len = max(max_len, child_len)

            if child.val - 1 == root.val:
                up = max(up, child_up + 1)

            if child.val + 1 == root.val:
                down = max(down, child_down + 1)

        max_len = max(down + 1 + up, max_len)

        return max_len, up, down
