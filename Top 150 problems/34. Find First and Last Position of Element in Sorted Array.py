class Solution(object):
    def searchRange(self, nums, target):
        left = self.helper(nums,target,True)
        right = self.helper(nums,target,False)
        return [left,right]

    
    def helper(self,nums,target,leftbias):
        l,r= 0,len(nums)-1
        i = -1
        while l <= r:
            mid = (l+r)//2
            if target>nums[mid]:
                l = mid + 1
            elif target<nums[mid]:
                r = mid - 1
            else:
                i = mid
                if leftbias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i

        
