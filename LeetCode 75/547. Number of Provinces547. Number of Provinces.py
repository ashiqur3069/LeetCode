class Solution:
    def findCircleNum(self, isConnected):
        numProvinces = 0
        n = len(isConnected)
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                numProvinces += 1
                self.dfs(isConnected, i, visited)
        
        return numProvinces
    
    def dfs(self, isConnected, i, visited):
        if visited[i]:
            return
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] and not visited[j]:
                self.dfs(isConnected, j, visited)
