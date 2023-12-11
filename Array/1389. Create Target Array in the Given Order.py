class Solution(object):
    def createTargetArray(self, nums, index):
        target =[]
        for i in range(len(nums)):
            if index[i] == len(target) :
                target.append(nums[i])
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target
      '''
class Solution:
    def createTargetArray(self, nums, index):
        a=[]
        for i in range(len(nums)):
            a.insert(index[i],nums[i])
        return a
      '''
