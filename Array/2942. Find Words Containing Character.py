class Solution(object):
    def findWordsContaining(self, words, x):
        array = []
        for i in range(len(words)):
            if x in words[i]:
                array.append(i)
        return array
