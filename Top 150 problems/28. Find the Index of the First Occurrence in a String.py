class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
   '''
        l=len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+l]==needle:
                return i
        return -1
        
  '''
