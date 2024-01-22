class Solution(object):
    def longestCommonPrefix(self, strs):
        com_pre = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return com_pre
            com_pre += strs[0][i]
        return com_pre
