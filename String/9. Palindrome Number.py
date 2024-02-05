class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or ( x!= 0 and x % 10 == 0):
            return False
        middle = 0
        while x > middle:
            middle = (x % 10 ) +  (middle * 10)
            x = x // 10
        return x == middle or  x == middle//10
