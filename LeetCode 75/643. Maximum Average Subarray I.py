class Solution(object):
    def findMaxAverage(self, nums, k):
        kth_sum = 0
        for i in range(k):
            kth_sum += nums[i]
        max_sum = kth_sum

        for j in range(k,len(nums)):
            kth_sum -= nums[j-k]
            kth_sum += nums[j]

            if max_sum < kth_sum:
                max_sum = kth_sum

        return (max_sum/(k*1.00))
