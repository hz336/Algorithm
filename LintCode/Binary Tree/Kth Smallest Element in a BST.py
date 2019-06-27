"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Notice
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example
Given root = {1,#,2}, k = 2, return 2.

Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest
routine?
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

""" O(h + k) time complexity """
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def __init__(self):
        self.index = 0
        self.kth = None

    def kthSmallest(self, root, k):
        # write your code here
        self.dfs(root, k)
        return self.kth

    def dfs(self, root, k):
        if root is None:
            return

        self.dfs(root.left, k)
        self.index += 1
        if self.index == k:
            self.kth = root.val

        if self.index < k:
            self.dfs(root.right, k)

"""
Challenge:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?

Answer: 
在 TreeNode 中增加一个 counter，代表整个树的节点个数
也可以用一个 HashMap<TreeNode, Integer> 来存储某个节点为代表的子树的节点个数
在增删查改的过程中记录不断更新受影响节点的 counter
在 kthSmallest 的实现中用类似 Quick Select 的算法去找到 kth smallest element
时间复杂度为 O(h)，h 为树的高度。
"""



























