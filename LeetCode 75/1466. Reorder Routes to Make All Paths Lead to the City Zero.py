class Solution(object):
    def minReorder(self, n, connections):
        graph = defaultdict(list)
        edges = set()
        for u,v in connections:
            edges.add((u,v))
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        self.changes = 0

        def dfs(city):
            for i in graph[city]:
                if i in visited:
                    continue
                if (i,city) not in edges:
                    self.changes += 1
                visited.add(i)
                dfs(i)
        visited.add(0)
        dfs(0)
        return self.changes

            
                
