class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l +=1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
        
