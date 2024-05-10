class Solution(object):
    def uniqueOccurrences(self, arr):
        unique_set = set()
        freq = {}

        for i in arr:
            freq[i] = freq.get(i,0) + 1
        for i in freq.values():
            if i in unique_set:
                return False
            unique_set.add(i)
        return True
