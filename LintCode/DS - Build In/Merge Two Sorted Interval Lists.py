"""
Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

Notice
The intervals in the given list do not overlap.
The intervals in different lists may overlap.
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here
        if len(list1) == 0:
            return list2

        if len(list2) == 0:
            return list1

        list3 = list1 + list2
        list3.sort(key=lambda x: x.start)
        results = []
        for interval in list3:
            if len(results) == 0 or results[-1].end < interval.start:
                results.append(interval)
            else:
                results[-1].end = max(results[-1].end, interval.end)

        return results


