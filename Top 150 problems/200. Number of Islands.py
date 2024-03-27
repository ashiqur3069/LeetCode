class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        rows,  cols = len(grid), len(grid[0])
        visited = set()
        island = 0
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]

                for i,j in direction:
                    new_row, new_col = row + i, col + j
                    if (new_row in range(rows) and
                        new_col in range(cols) and
                        grid[new_row][new_col] == "1" and 
                        (new_row,new_col) not in visited):
                        q.append((new_row,new_col))
                        visited.add((new_row,new_col))

                    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    island += 1
        return island

        



