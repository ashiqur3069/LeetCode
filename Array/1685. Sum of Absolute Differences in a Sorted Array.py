
"""
QUESTION: 

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation 
of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

Example 1:
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5

"""


class Solution(object):
    def getSumAbsoluteDifferences(self, nums):  
        total_sum = sum(nums)      #Here Calculate the total sum
        n = len(nums)              #Get total length
        running_sum = 0            # Find to sums by every iteration
        array = []
        for i in range(n):   
            running_sum += nums[i]    
            array.append((i+1) * nums[i] - running_sum + (total_sum-running_sum)-(n-i-1) * nums[i])

        return array

        
            ''' The pattern is for each element: for the first element 5(index[2]) :

            (index + 1) which is 3 then multiplied with the element to get (3*5) = 15 then minus pre-sum sum which is 2+3+5 = 10

            so we get (15 - 10) = 5 then add with it the total sum - running (10 - 10) = 0 - [(len 3 - 2[index] - 1) * 5] = 0

            then the answer will be only  5
            
            Now repeat with every element


            '''

     
