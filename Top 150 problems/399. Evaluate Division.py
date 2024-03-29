class Solution(object):
    def calcEquation(self, equations, values, queries):
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            first, second =eq
            adj[first].append([second,values[i]])
            adj[second].append([first,1/values[i]])
        def bfs(source,target):
            if source not in adj or target not in adj:
                return -1
            q, visited = deque(), set()
            q.append([source,1])
            visited.add(source)
            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for nei, cost in adj[node]:
                    if nei not in visited:
                        q.append([nei, weight * cost])
                        visited.add(nei)
            return -1
        return [bfs(q[0],q[1]) for q in queries]


        
