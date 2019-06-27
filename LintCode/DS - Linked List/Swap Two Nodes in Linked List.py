"""
Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, do nothing.

Notice: You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @param: v1: An integer
    @param: v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy_node = ListNode(0)
        dummy_node.next = head

        prev1, prev2 = self.find_previous(dummy_node, v1, v2)

        if prev1 is None or prev2 is None:
            return head

        if prev1 == prev2:
            return head

        if prev1.next == prev2:
            self.swap_adjacent(prev1)
        elif prev2.next == prev1:
            self.swap_adjacent(prev2)
        else:
            self.swap_remote(prev1, prev2)

        return dummy_node.next

    def find_previous(self, dummy_node, v1, v2):
        # Find the previous node in linked list
        prev1, prev2 = None, None

        p = dummy_node
        while p.next is not None:
            if p.next.val == v1:
                prev1 = p
            if p.next.val == v2:
                prev2 = p
            p = p.next

        return prev1, prev2

    def swap_adjacent(self, prev):
        # Swap the input node with its next node
        node1 = prev.next
        node2 = node1.next
        post = node2.next

        node1.next = post
        node2.next = node1
        prev.next = node2

    def swap_remote(self, prev1, prev2):
        # Swap two remote nodes
        node1 = prev1.next
        post1 = node1.next
        node2 = prev2.next
        post2 = node2.next

        prev1.next = node2
        node2.next = post1
        prev2.next = node1
        node1.next = post2

