"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
Time Complexity: O(m + n)
Space Complexity: O(1)
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy = ListNode(0)
        p = dummy
        left, right = l1, l2

        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next

            p = p.next

        if left:
            p.next = left

        if right:
            p.next = right

        return dummy.next



