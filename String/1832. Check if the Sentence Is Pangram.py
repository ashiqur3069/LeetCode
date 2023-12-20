'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 
'''
class Solution(object):
    def checkIfPangram(self, sentence):
        for i in range(ord('a'),ord("z")+1):
            if chr(i) not in sentence:
                return False
        return True
