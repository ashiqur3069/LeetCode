class Solution(object):
    def productExceptSelf(self, nums):
        array = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            array[i] = prefix
            prefix *= nums[i]
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            array[i] *= postfix
            postfix *= nums[i]
        return array
'''
        length = len(nums)
        products = [1] * length
        for i in range(1, length): # For first element we do not need to calculate
            products[i] = products[i-1] * nums[i-1]   # We do multiplication with the i element with previous 
                                                      # all and put it in i th position 

        right = nums[-1]  # Initially took last element because no element on the right
        for i in range(length-2, -1, -1):   # from the 2nd last element 
                                            # we multiply i th with the right value and and increse the 
                                            # right by multipling with the i th value
            products[i] *= right
            right *= nums[i]
        
        return products
        '''
