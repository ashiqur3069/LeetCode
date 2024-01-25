class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 1, len(numbers) 
        while l < r :
            sum = numbers[l-1] + numbers[r-1]
            
            if sum > target:
                r -= 1
            elif sum < target:
                 l += 1
            else:
                return [l,r]
