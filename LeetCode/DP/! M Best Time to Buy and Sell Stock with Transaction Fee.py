"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""

"""
Transition Equation 
sell[i] = max(sell[i - 1], buy[i - 1] + price[i - 1] - fee)
buy[i] = max(buy[i - 1], sell[i - 1] - price[i - 1])
"""

"""
考虑每一天同时维护两种状态：拥有股票(buy)状态和已经售出股票(sell)状态。用buy和sell分别保留这两种状态到目前为止所拥有的最大利润。 
对于sell，用前一天buy状态转移，比较卖出持有股是否能得到更多的利润，即sell = max(sell , buy + price - fee)， 
而对于sell, 我们考虑是否买新的股票更能赚钱(换言之，更优惠），buy = max(buy, sell-price)。
初始化我们要把sell设为0表示最初是sell状态且没有profit，把buy设为负无穷因为最初不存在该状态，我们不希望从这个状态进行转移
因为我们保存的都是最优状态，所以在买卖股票时候取max能保证最优性不变
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        num_days = len(prices)
        sell = [0] * (num_days + 1)
        buy = [float('-inf')]  * (num_days + 1)
        for i in range(1, num_days + 1): 
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i - 1] - fee)
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i - 1])
        
        return sell[num_days]


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0 
        buy = float('-inf')
        for price in prices: 
            sell = max(sell, buy + price - fee)
            buy = max(buy, sell - price)
        
        return sell
     
