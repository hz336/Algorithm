"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Have you met this question in a real interview?
Example
Given binary tree:

          1
         / \
        2   3
       / \
      4   5
Returns [[4, 5, 3], [2], [1]].
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
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """

    def findLeaves(self, root):
        # write your code here
        results = []
        self.dfs(root, results)
        return results

    def dfs(self, root, results):
        if root is None:
            return 0

        left_depth = self.dfs(root.left, results)
        right_depth = self.dfs(root.right, results)
        depth = max(left_depth, right_depth) + 1

        if len(results) < depth:
            results.append([])

        results[depth - 1].append(root.val)

        return depth

