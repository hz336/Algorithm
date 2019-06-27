"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    # Version 1. Traverse - 亲力亲为
    def inorder_traversal(self, root):
        results = []
        self.dfs(root, results)
        return results

    def dfs(self, root, results):
        if root is None:
            return

        self.dfs(root.left, results)
        results.append(root.val)
        self.dfs(root.right, results)

    # Version 2. Divide Conquer - 让小弟干
    def inorder_dc(self, root):
        # write your code here
        if root is None:
            return []

        left_values = self.inorder_dc(root.left)
        right_values = self.inorder_dc(root.right)
        results = left_values + [root.val] + right_values

        return results

    # Version 3. Non-recursion == iterative
    def inorder_iterative(self, root):
        stack = []
        results = []
        current = root

        while current or len(stack):
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            results.append(current.val)
            current = current.right

        return results

