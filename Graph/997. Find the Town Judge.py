class Solution(object):
    def findJudge(self, n, trust):
        
        delta = defaultdict(int) # num of imcoming - outgoing = n-1

        for source, dest in trust:
            delta[source] -= 1
            delta[dest] += 1
        for i in range(1,n+1):
            if delta[i] == n - 1:
                return i
        return -1
        
