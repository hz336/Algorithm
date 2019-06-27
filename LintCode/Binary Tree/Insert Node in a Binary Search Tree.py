"""
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

Notice
You can assume there is no duplicate values in this tree + node.

Have you met this question in a real interview?
Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \
  3             3   6
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution_v1:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        root = self.dfs(root, node)
        return root

    def dfs(self, root, node):
        if root is None:
            return node

        if node.val < root.val:
            root.left = self.dfs(root.left, node)
        else:
            root.right = self.dfs(root.right, node)

        return root


class Solution_v2:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        curr = root
        while curr != node:
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                curr = curr.right

        return root








