class Solution(object):
    def hammingWeight(self, n):
        #return bin(n).count("1")
        count = 0
        while n:
            count += n % 2
            n  = n // 2

        return count
