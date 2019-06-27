"""
Description
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Have you met this question in a real interview?
Example
Given prices = [4,4,6,1,1,4,2,5], and k = 2, return 6.

Challenge
O(nk) time.
"""

import math


"""
Time Complexity: O(nk)
Space Complexity: O(nk), can be improved to O(k)
"""
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """

    def maxProfit(self, K, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0

        num_days = len(prices)
        num_states = 2 * K + 1

        if num_states >= num_days:
            result = 0
            for day in range(1, num_days):
                result += max(prices[day] - prices[day - 1], 0)
            return result

        f = [[0 for _ in range(num_states + 1)] for _ in range(num_days + 1)]
        for state in range(2, num_states + 1):
            f[0][state] = -math.inf

        for day in range(1, num_days + 1):
            # state 1, 3, 5: f[price][state] = max(f[price - 1][state], f[price - 1][state - 1] + prices[price - 1] - prices[price - 2])
            for state in range(1, num_states + 1, 2):
                f[day][state] = f[day - 1][state]
                if state > 1 and day > 1:
                    f[day][state] = max(f[day - 1][state], f[day - 1][state - 1] + prices[day - 1] - prices[day - 2])

            # states 2, 4: f[price][state] = max(f[price - 1][state - 1], f[price - 1][state] + prices[price - 1] - prices[price - 2])
            for state in range(2, num_states + 1, 2):
                f[day][state] = f[day - 1][state - 1]
                if day > 1:
                    f[day][state] = max(f[day - 1][state - 1], f[day - 1][state] + prices[day - 1] - prices[day - 2])

        result = -math.inf
        for state in range(1, num_states + 1, 2):
            result = max(result, f[num_days][state])

        return result