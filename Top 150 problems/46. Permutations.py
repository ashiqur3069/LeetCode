class Solution(object):
    def permute(self, nums):
        res = []
        def backtrack(nums,path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        backtrack(nums,[])
        return res
