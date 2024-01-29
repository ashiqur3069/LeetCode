class Solution(object):
    def twoSum(self, nums, target):
        nums = sorted((value, index) for index, value in enumerate(nums))
        l, r = 0, len(nums)-1

        while l < r:
            sm = nums[l][0] + nums[r][0]
            if sm > target:
                r -= 1
            elif sm < target:
                l +=1
            else:
                return [nums[l][1], nums[r][1]]
