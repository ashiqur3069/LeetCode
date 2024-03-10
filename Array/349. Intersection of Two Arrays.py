class Solution(object):
    def intersection(self, nums1, nums2):
        num1_set = set(nums1)
        result = set()
        for i in nums2:
            if i in num1_set:
                result.add(i)
        return list(result)
        
        
