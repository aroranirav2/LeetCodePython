class Solution:
    def maxProfit(prices: list[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            max_profit = max(prices[sell] - prices[buy], max_profit)
            sell += 1
            
        return max_profit
    
    print(maxProfit([7,1,5,3,6,4]))