"""
Given a collection of intervals, merge all overlapping intervals.
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        # write your code here
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x.start)
        results = []
        for interval in intervals:
            if len(results) == 0 or results[-1].end < interval.start:
                results.append(interval)
            else:
                results[-1].end = max(results[-1].end, interval.end)

        return results
