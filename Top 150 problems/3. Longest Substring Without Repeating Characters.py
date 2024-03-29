class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in res_set:
                res_set.remove(s[l])
                l += 1
            res_set.add(s[r])
            res = max(res, r - l + 1)
        return res
        '''
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length
    '''
