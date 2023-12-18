class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        for x in range(1,len(nums)):
            if nums[x-1] != nums[x]:
                nums[i] = nums[x]
                i+=1
        return i 
