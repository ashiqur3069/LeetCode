class Solution(object):
    def orangesRotting(self, grid):
        q = deque()
        rows, cols = len(grid), len(grid[0])

        time, fresh= 0, 0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for i, j in directions:
                    new_r, new_c = row + i, col + j
                    if (new_r < 0 or new_r == len(grid) or 
                        new_c < 0 or new_c == len(grid[0]) or
                        grid[new_r][new_c] != 1):
                        continue
                    grid[new_r][new_c] = 2
                    q.append([new_r, new_c])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
