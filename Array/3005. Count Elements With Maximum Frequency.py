class Solution(object):
    def maxFrequencyElements(self, nums):
        array = {}
        nums2 = set(nums)
        for i in nums2:
            array[i] = nums.count(i)
        max_fre = max(array.values())
        sums = 0
        for val in array.values():
            if val == max_fre:
                sums += val
        return (sums)
        
        
