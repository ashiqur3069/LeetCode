class Solution(object):
    def cellsInRange(self, s):
        lst = []
        for i in range(ord(s[0]),ord(s[3])+1):
            for j in range(int(s[1]),int(s[4])+1):
                lst.append(chr(i)+str(j))
        return lst
        
