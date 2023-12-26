class Solution(object):
    def maxProfit(self, prices):
        l = 0
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - prices[l]
            if profit > 0:
                max_profit = max(profit,max_profit)
            else:
                l = i
        return max_profit
        


