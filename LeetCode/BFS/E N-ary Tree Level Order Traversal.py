"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]

"""


# # Definition for a Node.
# class Node:
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        results = []
        while q:
            results.append([item.val for item in q])
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                for child in node.children:
                    q.append(child)

        return results
