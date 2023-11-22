class Solution(object):
    def buildArray(self, nums):
        new_nums = [0]*len(nums)
        for i in range (len(nums)):
            new_nums[i]=nums[nums[i]]
        return new_nums
nums = [0,2,1,5,3,4]
s = Solution()
r = s.buildArray(nums)
print(r)
