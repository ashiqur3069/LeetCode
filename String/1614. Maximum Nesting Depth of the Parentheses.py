class Solution(object):
    def maxDepth(self, s):
        ans = 0
        start = 0

        for i in s:
            if i == "(":
                start += 1
                ans = max(start,ans)
            elif i == ")":
                start -= 1
        return ans
        
        
