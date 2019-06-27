"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None:
            return

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left, right = left_dummy, right_dummy
        p = head
        while p:
            if p.val < x:
                left.next = p
                left = p
            else:
                right.next = p
                right = p

            p = p.next

        right.next = None
        left.next = right_dummy.next

        return left_dummy.next





