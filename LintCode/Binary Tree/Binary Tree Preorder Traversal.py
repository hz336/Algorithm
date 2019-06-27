"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    # Version 1. Traverse - 亲力亲为
    def preorder_traversal(self, root):
        results = []
        self.traverse(root, results)
        return results

    # 1. 递归的定义：
    # 把以root为根的二叉树的preorder丢进results里
    def traverse(self, root, results):
        # 3. 递归的出口
        if root is None:
            return

        # 2. 递归的拆解
        results.append(root.val)
        self.traverse(root.left, results)
        self.traverse(root.right, results)

    # Version 2. Divide Conquer - 让小弟干
    # 1. 递归的定义：求出以root为根的preorder并return
    def preorder_dc(self, root):
        # 1. 递归的出口
        if root is None:
            return []

        # 2. 递归的拆解
        left_values = self.preorder_dc(root.left)
        right_values = self.preorder_dc(root.right)
        results = [root.val] + left_values + right_values

        return results

    # Version 3. Non-recursion == iterative
    def preorder_iterative(self, root):
        # write your code here
        if root is None:
            return []

        stack = [root]
        results = []

        while stack:
            node = stack.pop()
            results.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return results


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

sol = Solution()
ans = sol.preorder_traversal(node1)
print(ans)

ans = sol.preorder_dc(node1)
print(ans)

ans = sol.preorder_iterative(node1)
print(ans)















