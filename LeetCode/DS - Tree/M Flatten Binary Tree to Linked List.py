"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def flatten(self, root):
        self.helper(root)

    def helper(self, root):
        if root is None:
            return

        left_last = self.helper(root.left)
        right_last = self.helper(root.right)

        # connect left_last to root.right
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        # if there is right subtree, last node in right subtree should be the last node in the combined substree
        if right_last:
            print("right_last is %s" % str(right_last.val))
            return right_last

        # if there is no right right subtree, but only left subtree, last node in left subtree should be the last node
        if left_last:
            print("left_last is %s" % str(left_last.val))
            return left_last

        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node5
node2.left = node3
# node2.right = node4
node5.right = node6

sol = Solution()
sol.flatten(node1)

p = node1
while p:
    print(p.val)
    p = p.right









