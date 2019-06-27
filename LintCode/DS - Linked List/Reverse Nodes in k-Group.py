"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """

    def reverseKGroup(self, head, k):
        # write your code here
        if head is None:
            return None

        dummy = ListNode(0, head)
        prev = dummy
        while prev:
            prev = self.reverse(prev, k)

        return dummy.next

    # head -> n1 -> n2 ... nk -> nk+1
    # =>
    # head -> nk -> nk-1 .. n1 -> nk+1
    # return n1
    def reverse(self, node, k):
        n1_prev = node
        n1 = node.next

        p = node
        for i in range(k):
            p = p.next
            if p is None:
                return
        nk = p
        nk_next = nk.next

        prev = node
        curr = prev.next
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        n1.next = nk_next
        n1_prev.next = nk

        return n1





