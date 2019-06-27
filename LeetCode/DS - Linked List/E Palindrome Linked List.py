"""
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # Find the middle node
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy.next, dummy.next.next
        while right.next and right.next.next:
            left = left.next
            right = right.next.next
        mid = left.next

        # Odd number
        if right.next:
            mid = mid.next

        # reverse list
        mid = self.revserse(mid)

        # compare two lists
        left, right = dummy.next, mid
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True

    def revserse(self, head):
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node


