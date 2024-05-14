class Solution(object):
    def removeStars(self, s):
        stk = []
        for i in s:
            if i != "*":
                stk.append(i)
            else:
                stk.pop()
        return "".join(stk)
