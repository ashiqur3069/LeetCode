class Solution(object):
    def beautifulArray(self, n):
        nums = [i for i in range(1,n+1)]
        def recursion(nums):
            if len(nums) < 3:
                return nums
            even = nums[::2]
            odd = nums[1::2]
            return recursion(even) + recursion(odd)
        return recursion(nums)
        
