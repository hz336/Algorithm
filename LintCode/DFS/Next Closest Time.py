"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit
can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example
Given time = "19:34", return "19:39".

Explanation:
The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59
minutes later.
Given time = "23:59", return "22:22".

Explanation:
The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than
the input time numerically.
"""

import math


class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """

    def __init__(self):
        self.min_diff = math.inf
        self.result = ""

    def nextClosestTime(self, time):
        # write your code here
        time_set = set(time)
        time_set.remove(":")
        digits = list(time_set)

        if len(digits) == 1:
            return time

        minutes = int(time[0: 2]) * 60 + int(time[3: 5])
        self.dfs(digits, "", 0, minutes)

        return self.result

    def dfs(self, digits, curr, index, target):
        if index == 4:
            minutes = int(curr[0: 2]) * 60 + int(curr[2: 4])
            if minutes == target:
                return

            if minutes > target:
                diff = minutes - target
            else:
                diff = 24 * 60 + minutes - target

            if diff < self.min_diff:
                self.min_diff = diff
                self.result = curr[0: 2] + ':' + curr[2: 4]

            return

        for i in range(len(digits)):
            if index == 0 and int(digits[i]) > 2:
                continue

            if index == 1 and int(curr) * 10 + int(digits[i]) > 23:
                continue

            if index == 2 and int(digits[i]) > 5:
                continue

            if index == 3 and int(curr[2]) * 10 + int(digits[i]) > 59:
                continue

            self.dfs(digits, curr + digits[i], index + 1, target)
