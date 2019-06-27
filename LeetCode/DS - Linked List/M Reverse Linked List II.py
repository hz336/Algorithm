"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head

        pre_mth_node = self.find_node(dummy_node, m - 1)
        mth_node = pre_mth_node.next
        nth_node = self.find_node(dummy_node, n)
        post_nth_node = nth_node.next
        nth_node.next = None

        self.reverse_node(mth_node)
        pre_mth_node.next = nth_node
        mth_node.next = post_nth_node

        return dummy_node.next

    def find_node(self, dummy_node, node_index):
        p = dummy_node
        for i in range(node_index):
            p = p.next

        return p

    def reverse_node(self, node):
        pre = None
        p = node

        while p is not None:
            next_node = p.next
            p.next = pre
            pre = p
            p = next_node

