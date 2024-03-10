class Solution(object):
    def getCommon(self, nums1, nums2):
        num1_set = set(nums1)
        for i in nums2:
            if i in num1_set:
                return i
        return -1
        
