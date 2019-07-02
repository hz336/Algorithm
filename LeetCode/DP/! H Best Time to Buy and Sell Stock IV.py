"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

"""
Time Complexity: O(nk)
Space Complexity: O(nk)
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        num_days = len(prices)
        num_states = 2 * k + 1        
        
        if num_states >= num_days:
            result = 0
            for day in range(1, num_days):
                result += max(prices[day] - prices[day - 1], 0)
            return result
        
        f = [[0 for _ in range(num_states + 1)] for _ in range(num_days + 1)]

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

        result = float('-inf')
        for state in range(1, num_states + 1, 2):
            result = max(result, f[num_days][state])

        return result        
     

    
"""
Time Complexity: O(nk)
Space Complexity: O(k)
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        num_days = len(prices)
        num_states = 2 * k + 1        
        
        if num_states >= num_days:
            result = 0
            for day in range(1, num_days):
                result += max(prices[day] - prices[day - 1], 0)
            return result
        
        f = [[0 for _ in range(num_states + 1)] for _ in range(2)]
        old, now = 0, 1
        
        for day in range(1, num_days + 1):
            old, now = now, old
            
            # state 1, 3, 5: f[price][state] = max(f[price - 1][state], f[price - 1][state - 1] + prices[price - 1] - prices[price - 2])
            for state in range(1, num_states + 1, 2):
                f[now][state] = f[old][state]
                if state > 1 and day > 1:
                    f[now][state] = max(f[old][state], f[old][state - 1] + prices[day - 1] - prices[day - 2])

            # states 2, 4: f[price][state] = max(f[price - 1][state - 1], f[price - 1][state] + prices[price - 1] - prices[price - 2])
            for state in range(2, num_states + 1, 2):
                f[now][state] = f[old][state - 1]
                if day > 1:
                    f[now][state] = max(f[old][state - 1], f[old][state] + prices[day - 1] - prices[day - 2])

        result = float('-inf')
        for state in range(1, num_states + 1, 2):
            result = max(result, f[now][state])

        return result        
        
