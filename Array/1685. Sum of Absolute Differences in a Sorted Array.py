class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        total_sum = sum(nums)
        n = len(nums)
        running_sum = 0
        array = []
        for i in range(n):
            running_sum += nums[i]
            array.append((i+1) * nums[i] - running_sum + (total_sum-running_sum)-(n-i-1) * nums[i])

        return array
