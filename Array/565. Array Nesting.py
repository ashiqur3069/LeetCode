class Solution(object):
    def arrayNesting(self, nums):
        def dfs(k):
            if k in visited:
                return 0
            visited.add(k)
            return 1 +dfs(nums[k])

        visited=set()
    
        ans=0
        for i in range(len(nums)):
            if i not in visited:
                ans=max(ans,dfs(i))
        return ans 
