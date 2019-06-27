"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return

        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA is not None:
            lenA += 1
            nodeA = nodeA.next

        while nodeB is not None:
            lenB += 1
            nodeB = nodeB.next

        nodeA, nodeB = headA, headB
        while lenA > lenB:
            nodeA = nodeA.next
            lenA -= 1

        while lenB > lenA:
            nodeB = nodeB.next
            lenB -= 1

        while nodeA is not nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA

