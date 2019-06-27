"""
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after
removing exactly one edge on the original tree.

Notice
The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000

Example
Given
    5
   / \
  10 10
    /  \
   2   3

return True
Explanation:
    5
   /
  10

Sum: 15

   10
  /  \
 2    3

Sum: 15
Given
    1
   / \
  2  10
    /  \
   2   20

return False

Explanation:
You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict


class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """

    def checkEqualTree(self, root):
        # write your code here
        mapping = defaultdict(int)
        total = self.get_total(root, mapping)

        if total == 0:
            return mapping[total] > 1

        return total % 2 == 0 and total // 2 in mapping

    def get_total(self, root, mapping):
        if root is None:
            return 0

        total = self.get_total(root.left, mapping) + self.get_total(root.right, mapping) + root.val
        mapping[total] += 1

        return total
