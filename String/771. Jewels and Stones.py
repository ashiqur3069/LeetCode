class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ans = 0
        for i in jewels:
            ans += stones.count(i)
        return ans
        
