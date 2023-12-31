
class Solution(object):
    def majorityElement(self, nums):
        res, count = 0, 0 
        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else -1)
        return res
