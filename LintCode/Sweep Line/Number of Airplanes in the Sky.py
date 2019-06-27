"""
Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

Notice
If landing and flying happens at the same time, we consider landing should happen at first.

Example
For interval list

[
  (1,10),
  (2,3),
  (5,8),
  (4,7)
]
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
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        if airplanes is None or len(airplanes) == 0:
            return 0

        tracker = []
        for i in range(len(airplanes)):
            tracker.append((airplanes[i].start, 1))
            tracker.append((airplanes[i].end, -1))

        tracker.sort(key=lambda x: (x[0], x[1]))

        total, num_max = 0, 0
        for t, delta in tracker:
            total += delta
            num_max = max(num_max, total)

        return num_max
