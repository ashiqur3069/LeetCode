class Solution(object):
    def findDiagonalOrder(self, nums):
        array = []  #first create a new array
        main_array = []  # This array returns the actual answer
        for i, j in enumerate(nums): # Iterate array by i = 0 and j = nums[index0]
            for k, value in enumerate(j):  # now for j we do the same here k = 0 and value = 1,2,3
                array.append((i+k, k, value)) #make a tuple and append to array
        array.sort()  # sort the array to find the values
        for i , j , k in array:
            main_array.append(k)  #iterate and add the main array list
        return main_array 
nums = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
r = s.findDiagonalOrder(nums)
print(r)
