"""
Given a binary tree, return all root-to-leaf paths.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    # Version 1. Divide Conquer
    # 1. 递归的定义
    def binaryTreePaths_dc(self, root):
        # 3. 递归的出口
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        # 2. 递归的拆解
        left_path = self.binaryTreePaths_dc(root.left)
        right_path = self.binaryTreePaths_dc(root.right)
        full_path = left_path + right_path

        results = []
        for path in full_path:
            results.append(str(root.val) + '->' + path)

        return results

    # Version 2. Traverse
    def binaryTreePaths_traverse(self, root):
        # Write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, tmp):
        tmp.append(str(node.val))
        if node.left is None and node.right is None:
            result.append('->'.join(tmp))
            tmp.pop()
            return

        if node.left:
            self.dfs(node.left, result, tmp)

        if node.right:
            self.dfs(node.right, result, tmp)

        tmp.pop()



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
ans = sol.binaryTreePaths_dc(node1)
print(ans)

ans = sol.binaryTreePaths_traverse(node1)
print(ans)