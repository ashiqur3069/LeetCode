class Solution(object):
    def maxSubarraySumCircular(self, nums):
        globmax, globmin = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0

        for i in nums:
            total += i
            curmax = max(curmax + i, i)
            curmin = min(curmin + i, i)
            globmax = max(globmax, curmax)
            globmin = min(globmin, curmin)

        return max(globmax, total-globmin) if globmax > 0 else globmax

        
