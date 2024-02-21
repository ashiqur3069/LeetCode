class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        cur_sum = 0

        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            max_sum = max(max_sum,cur_sum)
        return max_sum



            
