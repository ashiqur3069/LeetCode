class Solution(object):
    def truncateSentence(self, s, k):
        s1 = s.split(" ")
        return " ".join(s1[:k])

