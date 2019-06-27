"""
Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path does not
need to start or end at the root or a leaf, but it must go in a straight line down.

Example
Given a binary tree:

    1
   / \
  2   3
 /   /
4   2
for target = 6, return

[
  [2, 4],
  [1, 3, 2]
]
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
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        # write your code here
        path = []
        results = []
        self.dfs(root, target, path, results, 0)
        return results

    def dfs(self, root, target, path, results, depth):
        if root is None:
            return

        path.append(root.val)
        rest = target
        for i in range(depth, -1, -1):
            rest -= path[i]
            if rest == 0:
                results.append(path[i:])

        self.dfs(root.left, target, path, results, depth + 1)
        self.dfs(root.right, target, path, results, depth + 1)

        path.pop()


