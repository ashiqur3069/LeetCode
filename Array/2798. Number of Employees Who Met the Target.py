class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        num = 0
        for i in hours:
            if i>=target:
                num+=1
        return num
        
        
