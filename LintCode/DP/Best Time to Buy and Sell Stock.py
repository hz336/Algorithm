"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum
profit.

Example
Given array [3,2,3,1,2], return 1.
"""

import math


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0

        num_min = math.inf
        profit = 0
        for p in prices:
            num_min = min(num_min, p)
            profit = max(profit, p - num_min)

        return profit