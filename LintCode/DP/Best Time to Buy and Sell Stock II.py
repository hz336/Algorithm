"""
Description
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock
multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example
Given an example [2,1,2,0,1], return 2
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

        profit = 0
        for i in range(1, len(prices)):
            gain = max(0, prices[i] - prices[i - 1])
            profit += gain

        return profit
