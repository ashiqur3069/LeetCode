class Solution(object):
    def increasingTriplet(self, nums):
        s1 = s2 = float("inf")

        for n in nums:
            if n > s2:
                return True
            elif n <= s1:
                s1 = n
            else: 
                s2 = n
        return False

