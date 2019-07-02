"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

"""
Time Complexity: O(nk) with k = 2
Space Complexity: O(nk) with k = 2
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
    
"""
Time Complexity: O(nk) with k = 2
Space Complexity: O(k) with k = 2
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0
        
        num_days = len(prices)
        num_states = 2 * 2 + 1
        f = [[0 for _ in range(num_states + 1)] for _ in range(2)]
        old, now = 0, 1
        
        for day in range(1, num_days + 1): 
            old, now = now, old
            for state in range(1, num_states + 1, 2): 
                f[now][state] = f[old][state]
                if state > 1 and day > 1: 
                    f[now][state] = max(f[old][state], f[old][state - 1] + prices[day - 1] - prices[day - 2])
                    
            for state in range(2, num_states + 1, 2): 
                f[now][state] = f[old][state - 1]
                if day > 1:
                    f[now][state] = max(f[old][state] + prices[day - 1] - prices[day - 2], f[old][state - 1])
                
        result = float('-inf')
        for state in range(1, num_states + 1, 2):
            result = max(result, f[now][state])
        
        return result
    
