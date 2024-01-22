class Solution(object):
    def reverseWords(self, s):
        s = s.split(" ")
        rev_str = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].strip() != "":
                rev_str += s[i] + " "
        return rev_str[:-1]
            
        
