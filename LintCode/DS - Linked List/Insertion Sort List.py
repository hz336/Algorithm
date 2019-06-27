"""
Sort a linked list using insertion sort.

Example
Given 1->3->2->0->null, return 0->1->2->3->null.
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        # write your code here
        if head is None:
            return head

        dummy = ListNode(0, head)
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next

                temp = curr.next
                curr.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                curr = curr.next

        return dummy.next



