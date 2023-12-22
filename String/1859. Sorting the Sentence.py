class Solution(object):
    def sortSentence(self, s):
        array = {}
        s = s.split(" ")
        for i in s:
            array[int(i[-1])] = i[:-1]
        return " ".join(array.values())
