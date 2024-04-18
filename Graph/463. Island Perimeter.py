class Solution(object):
    def islandPerimeter(self, grid):
        visited = set()

        def dfs(i,j):
            if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            prmtr = dfs(i,j+1)
            prmtr += dfs(i,j-1)
            prmtr += dfs(i-1,j)
            prmtr += dfs(i+1,j)
            return prmtr
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
