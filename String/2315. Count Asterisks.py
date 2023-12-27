class Solution(object):
    def countAsterisks(self, s):
        s = s.split('|')
        c = 0
        for i in range(0,len(s),2):
            c += s[i].count('*')
        return c
       
