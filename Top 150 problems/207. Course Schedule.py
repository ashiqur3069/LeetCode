class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        pre_map = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        print(pre_map)
        visitset = set()

        def dfs(crs):
            if crs in visitset:
                return False
            if pre_map[crs] == []:
                return True
            visitset.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):return False
            visitset.remove(crs)
            pre_map[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
          
