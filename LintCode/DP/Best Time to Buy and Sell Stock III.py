"""
Description
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example
Given an example [4,4,6,1,1,4,2,5], return 6.
"""

import math


"""
Time Complexity: O(n)
Space Complexity: O(n), can be improved to O(1)
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0

        num_days = len(prices)
        num_states = 2 * 2 + 1
        f = [[0 for _ in range(num_states + 1)] for _ in range(num_days + 1)]
        for state in range(2, num_states + 1):
            f[0][state] = -math.inf

        for day in range(1, num_days + 1):
            # state 1, 3, 5: f[day][state] = max(f[day - 1][state], f[day - 1][state - 1] + prices[day - 1] - prices[day - 2])
            for state in range(1, num_states + 1, 2):
                f[day][state] = f[day - 1][state]
                if day > 1 and state > 1:
                    f[day][state] = max(f[day][state], f[day - 1][state - 1] + prices[day - 1] - prices[day - 2])

            # states 2, 4: f[day][state] = max(f[day - 1][state - 1], f[price - 1][state] + prices[price - 1] - prices[price - 2])
            for state in range(2, num_states + 1, 2):
                f[day][state] = f[day - 1][state - 1]
                if day > 1:
                    f[day][state] = max(f[day][state], f[day - 1][state] + prices[day - 1] - prices[day - 2])

        result = -math.inf
        for state in range(1, num_states + 1, 2):
            result = max(result, f[num_days][state])

        return result

