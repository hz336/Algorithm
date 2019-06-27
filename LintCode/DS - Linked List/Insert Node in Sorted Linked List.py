"""
Insert a node in a sorted linked list.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """

    def insertNode(self, head, val):
        # write your code here
        dummy = ListNode(0, head)

        p = dummy
        while p.next and p.next.val < val:
            p = p.next

        node = ListNode(val, next=p.next)
        p.next = node

        return dummy.next
