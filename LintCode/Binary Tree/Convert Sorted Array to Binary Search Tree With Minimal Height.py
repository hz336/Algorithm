"""
Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.

Notice
There may exist multiple valid solutions, return any of them.

Have you met this question in a real interview?
Example
Given [1,2,3,4,5,6,7], return

     4
   /   \
  2     6
 / \    / \
1   3  5   7
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
    @param: A: an integer array
    @return: A tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return

        root = self.dfs(A)
        return root

    def dfs(self, A):
        if len(A) == 0:
            return

        start, end = 0, len(A) - 1
        mid = start + (end - start) // 2

        root = TreeNode(A[mid])
        root.left = self.dfs(A[: mid])
        root.right = self.dfs(A[mid + 1:])

        return root