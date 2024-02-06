class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        book1 = {}

        if len(s) != len(pattern):
            return False
        
        index = 0

        for i in range(len(s)):
            if s[i] not in book1:
                if pattern[i] in book1.values():
                    return False
                book1[s[i]] = pattern[i]
            if book1[s[i]] != pattern[i]:
                return False

        return True
       
