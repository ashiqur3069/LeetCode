class Solution(object):
    def maxOperations(self, nums, k):
        ans = 0
        counts = dict()
        for n in nums:
            seeking = k - n
            if seeking in counts and (counts[seeking] > 0):
                ans += 1
                counts[seeking] -= 1
                continue
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        return ans
            
