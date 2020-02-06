"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None, ]

        all_trees = []
        for i in range(start, end + 1):  # pick up a root
            # all possible left subtrees if i is choosen to be a root
            left_trees = self.dfs(start, i - 1)

            # all possible right subtrees if i is choosen to be a root
            right_trees = self.dfs(i + 1, end)

            # connect left and right subtrees to the root i
            for l in left_trees:
                for r in right_trees:
                    curr_tree = TreeNode(i)
                    curr_tree.left = l
                    curr_tree.right = r
                    all_trees.append(curr_tree)

        return all_trees

