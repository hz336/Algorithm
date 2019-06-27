"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of the linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        dummy = ListNode(0, head)

        parent = dummy
        cur = parent.next

        while cur and cur.next:
            if cur.val == cur.next.val:
                value = cur.val
                while cur and value == cur.val:
                    cur = cur.next
                parent.next = cur
            else:
                cur = cur.next
                parent = parent.next

        return dummy.next

