"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return

        self.copy_next(head)
        self.copy_random(head)
        new_head = self.split(head)
        return new_head

    def copy_next(self, head):
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            node.random = p.random
            p.next = node
            p = p.next.next

    def copy_random(self, head):
        p = head
        while p:
            if p.next.random:
                p.next.random = p.random.next
            p = p.next.next

    def split(self, head):
        new_head = head.next
        p = head
        while p:
            tmp = p.next
            p.next = tmp.next
            p = p.next
            if tmp.next:
                tmp.next = tmp.next.next

        return new_head

