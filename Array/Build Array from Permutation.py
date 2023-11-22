class Solution(object):
    def buildArray(self, nums):
        new_nums = [0]*len(nums) #here create a new array same as given array
        for i in range (len(nums)):
            new_nums[i]=nums[nums[i]]  #iterate the given array, find the index and put it on new array
        return new_nums
nums = [0,2,1,5,3,4]
s = Solution()
r = s.buildArray(nums)
print(r)
