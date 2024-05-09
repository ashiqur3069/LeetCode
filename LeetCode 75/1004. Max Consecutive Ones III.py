class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        n = len(nums)
        zeros = 0
        max_window = 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            w = r-l+1
            max_window = max(w,max_window)
        return max_window




