"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


"""
Best Answer: Merge Sort
Time Complexity: O(nlogk). O(logk) layers with O(n) for merging per layer. 
Space Complexity: O(1) 
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return

        result = self.merge_helper(lists, 0, len(lists) - 1)

        return result

    def merge_helper(self, lists, start, end):
        if start >= end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_helper(lists, start, mid)
        right = self.merge_helper(lists, mid + 1, end)

        return self.merge_two_lists(left, right)

    def merge_two_lists(self, list1, list2):
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        if list1 is None:
            p.next = list2

        if list2 is None:
            p.next = list1

        return dummy.next


"""
Priority Queue
Time Complexity: O(nlogk). Insertion into a min heap takes O(logk), and there are N points in total.
Space Complexity: O(k) for priority queue.
"""
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return

        heap = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index, node))

        dummy = ListNode(0)
        p = dummy
        while heap:
            value, index, node = heapq.heappop(heap)
            p.next = node
            p = p.next

            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

        return dummy.next

