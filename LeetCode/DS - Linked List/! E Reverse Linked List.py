"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head is None or head.next is None:
            return head

        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node
