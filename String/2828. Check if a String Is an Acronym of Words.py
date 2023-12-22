class Solution(object):
    def isAcronym(self, words, s):
        new_word = ''
        for i in words:
            new_word += i[0]
        return True if new_word == s else False
