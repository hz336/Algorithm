"""
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    """
    Algorithm: Traverse
    
    Use recursion to traverse the tree in preorder, pass with a parameter
    `sum` as the sum of each node from root to current node.
    Put the whole path into result if the leaf has a sum equal to target.
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        path = []
        results = []
        self.dfs(root, path, results, 0, target)
        return results

    def dfs(self, root, path, results, cur, target):
        if root is None:
            return

        cur += root.val
        path.append(root.val)

        if root.left is None and root.right is None and cur == target:
            results.append(path[:])

        self.dfs(root.left, path, results, cur, target)
        self.dfs(root.right, path, results, cur, target)

        path.pop()
