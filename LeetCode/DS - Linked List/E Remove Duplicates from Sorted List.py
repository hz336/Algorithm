"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        left = right = head
        while right:
            while right and left.val == right.val:
                right = right.next

            left.next = right
            left = left.next

        return dummy.next
