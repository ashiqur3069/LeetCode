class Solution(object):
    def isIsomorphic(self, s, t):
        dic1, dic2 = {}, {}
        for c1, c2 in zip(s,t):
            if ((c1 in dic1 and dic1[c1] != c2) or
            (c2 in dic2 and dic2[c2] != c1)) :
                return False
        
            dic1[c1] = c2
            dic2[c2] = c1
        return True
        '''
        z=zip(s,t)
        if len(set(z))==len(set(s))==len(set(t)):
            return True
        return False
        '''
