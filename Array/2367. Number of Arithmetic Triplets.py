class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        ans = 0
        for i in range(len(nums)):
            if (nums[i] - diff) in nums and (diff + nums[i]) in nums:
                ans += 1
        return ans
