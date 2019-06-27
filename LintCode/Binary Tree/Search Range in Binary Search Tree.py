"""
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x
such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.

Have you met this question in a real interview?
Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def __init__(self):
        self.results = []

    def searchRange(self, root, k1, k2):
        # write your code here
        self.dfs(root, k1, k2)
        return self.results

    def dfs(self, root, k1, k2):
        if root is None:
            return

        if root.val > k1:
            self.dfs(root.left, k1, k2)

        if k1 <= root.val <= k2:
            self.results.append(root.val)

        if root.val < k2:
            self.dfs(root.right, k1, k2)

