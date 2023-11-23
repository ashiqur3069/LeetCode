class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0    #for count how many match with others
        for i in range(len(nums)):  #first iterate the array and took the element
            for j in range(i+1,len(nums)):  
              #from the second element to the last we check whether any common element can be found 
              #then increase the count by 1
                if nums[j]==nums[i]:
                    count+=1
        return count
nums = [1,2,3,1,1,3]
solution = Solution()
Result = solution.numIdenticalPairs(nums)
print(Result)
