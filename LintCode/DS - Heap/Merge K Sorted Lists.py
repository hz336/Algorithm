"""
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

""" 
Priority Queue
Time Complexity: O(nlogk)
"""
import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return

        if len(lists) == 1:
            return lists[0]

        heap = []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        dummy = ListNode(0)
        p = dummy
        while heap:
            p.next = ListNode(heapq.heappop(heap))
            p = p.next

        return dummy.next


""" 
Divide Conquer - Top Down method
Time Complexity: O(nlogk)
"""


class Solution_v1:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
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
Botoom Up method - Merge two by two 
Time Complexity: O(nlogk)
"""


class Solution_v2:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return

        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists) - 1, 2):
                merged_lists = self.merge_two_lists(lists[i], lists[i + 1])
                new_lists.append(merged_lists)
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])

            lists = new_lists

        return lists[0]

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

    