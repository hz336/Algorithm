"""
In a binary search tree, (Only) two nodes are swapped. Find out these nodes and swap them. If there no node swapped, return original root of tree.

Example
Given a binary search tree:

    4
   / \
  5   2
 / \
1   3
return

    4
   / \
  2   5
 / \
1   3
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
    @param root: the given tree
    @return: the tree after swapping
    """

    def __init__(self):
        self.inorder = []

    def bstSwappedNode(self, root):
        # write your code here
        if root is None:
            return

        self.dfs(root)

        prev = post = -1
        flag = 0
        for i in range(len(self.inorder) - 1):
            if self.inorder[i] > self.inorder[i + 1]:
                if flag == 0:
                    prev = i
                    flag = 1
                else:
                    post = i + 1

        if prev == -1:
            return root

        if post == -1:
            post = prev + 1

        self.swap(root, self.inorder[prev], self.inorder[post])

        return root

    def swap(self, root, prev, post):
        if root is None:
            return

        self.swap(root.left, prev, post)

        if root.val == prev:
            root.val = post
        elif root.val == post:
            root.val = prev

        self.swap(root.right, prev, post)

    def dfs(self, root):
        if root is None:
            return

        self.dfs(root.left)
        self.inorder.append(root.val)
        self.dfs(root.right)

