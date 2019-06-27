"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    # Version 1. Traverse - 亲力亲为
    def postorder_traversal(self, root):
        results = []
        self.traverse(root, results)
        return results

    def traverse(self, root, results):
        if root is None:
            return

        self.traverse(root.left, results)
        self.traverse(root.right, results)
        results.append(root.val)

    # Version 2. Divide Conquer - 让小弟干
    def postorder_dc(self, root):
        # write your code here
        if root is None:
            return []

        left_values = self.postorder_dc(root.left)
        right_values = self.postorder_dc(root.right)
        results = left_values + right_values + [root.val]

        return results

