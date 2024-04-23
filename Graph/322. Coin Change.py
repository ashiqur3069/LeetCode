class Solution(object):
    def coinChange(self, coins, amount):
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0
        # for a in range(1,amount+1):
        #     for c in coins:
        #         if a-c>=0:
        #             dp[a] = min(dp[a], 1+dp[a-c])
        # return dp[amount] if dp[amount] != amount + 1 else -1
        queue=[]
        queue.append((0,0))
        visited=set()
        visited.add(0)
        while queue:
            sum_num,path=queue.pop(0)
            if sum_num==amount:
                return path
            for n in coins:
                if sum_num+n not in visited and sum_num+n <=amount:
                    queue.append((sum_num+n,path+1))
                    visited.add(sum_num+n)
        return -1
