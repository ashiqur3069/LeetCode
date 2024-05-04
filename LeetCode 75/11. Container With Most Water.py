class Solution(object):
    def maxArea(self, height):
        area = 0
        l, r =  0, len(height) - 1 
        while l < r :
            ins_area =  (r - l) * min (height[l], height[r])
            area = max(area, ins_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area
