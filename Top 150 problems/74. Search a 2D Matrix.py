class Solution(object):
    def searchMatrix(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            mid = (l + r) // 2
            value = matrix[mid//col][mid % col]
            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            else:
                return True
        return False

        
