class Solution(object):
    def restoreString(self, s, indices):
        shu_str = [""]*len(s)
        for i, x in enumerate(s):
            shu_str[indices[i]] = x
        return "".join(shu_str)

    '''
        ans = ""
        for i in range(len(indices)):
            ans += s[indices.index(i)]     [ here finding the value of indexes and then find the coresponding strings ]
        return ans
'''
