"""
Give two users' ordered online time series, and each section records the user's login time point x and offline time point y. Find out the time periods when both users are online at the same time, and output in ascending order.

Notice
We guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.

Example
Given seqA = [(1,2),(5,100)], seqB = [(1,6)], return [(1,2),(5,6)].

Explanation:
In these two time periods (1,2),(5,6), both users are online at the same time.
Given seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)], return [].

Explanation:
There is no time period, both users are online at the same time.
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    def timeIntersection(self, seqA, seqB):
        # Write your code here
        if seqA is None or seqB is None:
            return []

        if len(seqA) == 0 or len(seqB) == 0:
            return []

        seq = seqA + seqB

        tracker = []
        for i in range(len(seq)):
            tracker.append((seq[i].start, 1))
            tracker.append((seq[i].end, -1))

        tracker.sort(key=lambda x: (x[0], x[1]))

        results = []
        prev, curr = 0, 0
        start, end = 0, 0
        for t, delta in tracker:
            curr += delta

            if curr == 2 and prev == 1:
                start = t

            if curr == 1 and prev == 2:
                end = t
                results.append((start, end))

            prev = curr

        return results