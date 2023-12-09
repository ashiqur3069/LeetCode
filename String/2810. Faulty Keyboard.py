class Solution(object):
    def finalString(self, s):
        present = ''
        for i in s:
            if i =="i":
                present = present[::-1]
            else:
                present+=i
        return present
