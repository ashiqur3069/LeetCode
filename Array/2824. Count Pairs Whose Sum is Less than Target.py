'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 

'''

class Solution(object):
    def countPairs(self, nums, target):
        n = len(nums)
        num_of_pair = 0
        for i in range(n):
            for j in range(n):
                if 0 <= i < j < n and nums[i] + nums[j] < target:
                    num_of_pair +=1
        return num_of_pair
        
