class Solution(object):
    def shuffle(self, nums, n):
        new_array = []
        for i in range(n):
            new_array.append(nums[i])
            new_array.append(nums[n+i])
        return new_array
