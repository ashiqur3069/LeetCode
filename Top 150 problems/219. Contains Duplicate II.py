class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and abs(i - dic[v]) <= k:
                return True
            dic[v] = i
        return False
