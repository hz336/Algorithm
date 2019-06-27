"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll
have D linked lists).
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []

        results = []
        queue = deque([root])
        while queue:
            dummy = ListNode(0)
            pre = dummy
            for node in queue:
                curr = ListNode(node.val)
                pre.next = curr
                pre = curr

            results.append(dummy.next)

            len_q = len(queue)
            for _ in range(len_q):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return results

