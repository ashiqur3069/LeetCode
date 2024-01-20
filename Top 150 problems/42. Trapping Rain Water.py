class Solution(object):
    def trap(self, height):
        # if not height : return 0
        # l, r = 0, len(height)-1
        # leftmax , rightmax = height[l] , height[r]
        # res = 0
        # while l < r:
        #     if leftmax < rightmax:
        #         l += 1
        #         leftmax = max(leftmax, height[l])
        #         res += leftmax - height[l]
        #     else:
        #         r -=1
        #         rightmax = max(rightmax,height[r])
        #         res += rightmax - height[r]
        # return res
        left, right = 0, len(height) - 1
        water = 0

        while left < right:
            min_height = min(height[left], height[right])

            # Move the pointer with the lower min_height, ensuring we only
            # consider elements within the current boundaries
            while left < right and height[left] <= min_height:
                water += min_height - height[left]
                left += 1

            while left < right and height[right] <= min_height:
                water += min_height - height[right]
                right -= 1

        return water
