# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def maxProfit(self, prices):
    # here we just have to find max profit, can buy and sell numerous times
    profit = 0
    
    # The key point is we need to consider every peak immediately following
    # a valley to maximize the profit.
    for i in range(1, len(prices)):
        if(prices[i-1] < prices[i]):
            profit = profit + (prices[i]-prices[i-1])
    
    return profit