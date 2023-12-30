class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        citations.sort()
        for idx , val in enumerate(citations):
            if n - idx <= val:
                return n - idx
        return 0
        
