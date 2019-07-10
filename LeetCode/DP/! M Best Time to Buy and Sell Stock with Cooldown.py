"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock
multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_days = len(prices)
        buy = [float('-inf')] * (num_days + 1)
        sell = [0] * (num_days + 1)
        
        for i in range(1, num_days + 1): 
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i - 1])
            if i == 1: 
                buy[i] = max(buy[i - 1], 0 - prices[i - 1])
            else: 
                buy[i] = max(buy[i - 1], sell[i - 2] - prices[i - 1])
            
        return sell[num_days]


