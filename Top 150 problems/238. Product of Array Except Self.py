class Solution(object):
    def productExceptSelf(self, nums):
        array = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            array[i] = prefix
            prefix *= nums[i]
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            array[i] *= postfix
            postfix *= nums[i]
        return array
