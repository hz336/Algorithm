"""
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.

Example
Given binary tree:

    1
   / \
  2   3
 /
4
and target = 6. Return :

[
  [2, 4],
  [2, 1, 3],
  [3, 1, 2],
  [4, 2]
]
"""

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum3(self, root, target):
        # write your code here
        results = []
        self.dfs(root, target, results)
        return results

    def dfs(self, root, target, results):
        if root is None:
            return

        path = []
        self.find_sum(root, None, target, results, path)

        self.dfs(root.left, target, results)
        self.dfs(root.right, target, results)

    def find_sum(self, root, father, target, results, path):
        if root is None:
            return

        path.append(root.val)
        target -= root.val

        if target == 0:
            results.append(path[:])

        if root.parent not in [None, father]:
            self.find_sum(root.parent, root, target, results, path)

        if root.left not in [None, father]:
            self.find_sum(root.left, root, target, results, path)

        if root.right not in [None, father]:
            self.find_sum(root.right, root, target, results, path)

        path.pop()

