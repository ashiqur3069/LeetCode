class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        array = []
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i]>nums[j]:
                    count += 1
            array.append(count)
        return array
