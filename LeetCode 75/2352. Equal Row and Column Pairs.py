class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        hash_map = {}
        count = 0
        for item in grid:
            if tuple(item) not in hash_map:
                hash_map[tuple(item)] = 1
            else:
                hash_map[tuple(item)] += 1
        
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            if tuple(col) in hash_map:
                count += hash_map[tuple(col)]
        return count
