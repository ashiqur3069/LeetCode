class Solution(object):
    def maxProfit(self, prices):
        '''
        l = 0
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - prices[l]
            if profit > 0:
                max_profit += profit
                l = i
            else:
                l = i
        return max_profit
        '''
        profit = 0 
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
