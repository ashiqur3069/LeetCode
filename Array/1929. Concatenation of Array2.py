class Solution(object):
    def getConcatenation(self, nums):
        new_array = [0]*(2*len(nums)) #create a double size of array of the given array
        for i in range(len(nums)):
            new_array[i]=nums[i]     # normally iterate one by one element to the new array
            new_array[len(nums)+i]=nums[i]  #add same element but from the middle of the new array
        return new_array
nums = [1,2,1]
solution = Solution()
result = solution.getConcatenation(nums)
print(result)
1929. Concatenation of Array
