class Solution(object):
    def decompressRLElist(self, nums):
        array = []
        i = 0
        while i < len(nums):
            for j in range(nums[i]):
                array.append(nums[i+1])
            i +=2
        return array
      
      '''
      Easy Way
        new_list = []
        for i in range(0, len(nums), 2):
            new_list += [nums[i+1]] * nums[i]

        return new_list
    '''
