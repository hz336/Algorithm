"""
Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max
(inclusive). The resulting tree should still be a valid binary search tree. So, if we get this tree as input:
http://www.ardendertat.com/wp-content/uploads/2012/01/bst.png

and we’re given min value as 5 and max value as 13, then the resulting binary search tree should be:
http://www.ardendertat.com/wp-content/uploads/2012/01/bst_trim.png

Example
Given binary search tree:
{8,3,10,1,6,#,14,#,#,4,7,13} and minVal = 5, maxVal = 13.

One possible answer: {8, 6, 10, #, 7, #, 13}
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
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """

    def trimBST(self, root, minimum, maximum):
        # write your code here
        root = self.dfs(root, minimum, maximum)
        return root

    def dfs(self, root, minimum, maximum):
        if root is None:
            return

        if minimum <= root.val <= maximum:
            root.left = self.dfs(root.left, minimum, maximum)
            root.right = self.dfs(root.right, minimum, maximum)
        elif root.val < minimum:
            root = self.dfs(root.right, minimum, maximum)
        else:
            root = self.dfs(root.left, minimum, maximum)

        return root
