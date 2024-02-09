class Solution(object):
    def isHappy(self, n):

        seen = set()
        while n:
            if n in seen: return False
            seen.add(n)

            total = 0
            while n:
                total, n = total + (n % 10)**2, n // 10 
            if total == 1: return True
            n = total         
        return False
      

'''
        used = []
        while(n>0):
            tmp = 0
            while(n>0):
                i = n%10

                tmp += i*i
                n = n//10

            if(tmp in used):
                return False
            else:
                used.append(tmp)

            if(tmp==1):
                return True
            
            n = tmp

        return False

        '''  
        
