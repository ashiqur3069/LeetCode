class Solution(object):
    def isPowerOfTwo(self, n):
        # for i in range(31):
        #     ans = 2 ** i
        #     if ans == n:
        #         return True
        # return False
        if n == 0:
            return False
        
        while n > 0:
            if n == 1:
                return True
            if n % 2 != 0:
                break
            n //= 2
        return False
