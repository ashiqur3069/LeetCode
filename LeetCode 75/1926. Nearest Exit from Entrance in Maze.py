class Solution(object):
    def nearestExit(self, maze, entrance):
        entrance = (entrance[0], entrance[1])
        q = deque([entrance])
        visited = set()
        visited.add(entrance)
        m, n = len(maze), len(maze[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        while q:
            lenq = len(q)
            for _ in range(lenq):
                i, j = q.popleft()
                if (i, j) != entrance and (i == 0 or i == m-1 or j == 0 or j == n-1) and maze[i][j] == ".":
                    return count
                for d in direction:
                    new = (i+d[0],j+d[1])
                    if 0<= new[0] < m and 0 <= new[1] < n and new not in visited and maze[new[0]][new[1]] == ".":
                        visited.add(new)
                        q.append(new)
            count += 1
        return -1






