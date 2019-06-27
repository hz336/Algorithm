"""
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and
right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the
root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the
input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right
subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.


Example
Given
  1
   \
    2
   / \
  3   4

return
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Given
         1
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

return
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
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
    @param root: a TreeNode
    @return: a list of integer
    """

    def boundaryOfBinaryTree(self, root):
        # write your code here
        if root is None:
            return []

        results = [root.val]
        self.left_bdry(root.left, results)
        self.leaves(root, results)
        self.right_bdry(root.right, results)

        return results

    def left_bdry(self, root, results):
        if root is None:
            return

        if root.left is None and root.right is None:
            return

        results.append(root.val)

        if root.left:
            self.left_bdry(root.left, results)
        else:
            self.left_bdry(root.right, results)

    def leaves(self, root, results):
        if root is None:
            return

        if root.left is None and root.right is None:
            results.append(root.val)

        self.leaves(root.left, results)
        self.leaves(root.right, results)

    def right_bdry(self, root, results):
        if root is None:
            return

        if root.left is None and root.right is None:
            return

        if root.right:
            self.right_bdry(root.right, results)
        else:
            self.right_bdry(root.left, results)

        results.append(root.val)



