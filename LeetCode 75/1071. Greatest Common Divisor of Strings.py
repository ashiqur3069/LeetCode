class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        def isdivisor(i):
            if len1 % i != 0 or len2 % i != 0:
                return False
            # make sure both multiply same
            divisor = str1[:i]
            return divisor * (len1 // i) == str1 and divisor * (len2 // i) == str2
        
        for i in range(min(len1,len2),0,-1):
            if isdivisor(i):
                return str1[:i]
        return ""
        
