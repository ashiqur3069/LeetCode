class Solution(object):
    def findDiagonalOrder(self, nums):
        array = []
        main_array = []
        for i, j in enumerate(nums):
            for k, value in enumerate(j):
                array.append((i+k, k, value))
        array.sort()
        for i , j , k in array:
            main_array.append(k)
        return main_array
nums = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
r = s.findDiagonalOrder(nums)
print(r)
