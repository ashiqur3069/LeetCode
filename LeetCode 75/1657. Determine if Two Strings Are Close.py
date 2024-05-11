class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(word1)):
            freq1[ord(word1[i])-ord("a")] += 1
            freq2[ord(word2[i])-ord("a")] += 1
            
        for i in range(26):
            if freq1[i] != 0 and freq2[i] != 0:
                continue
            if freq1[i] == 0 and freq2[i] == 0:
                continue
            return False
        
        freq1.sort()
        freq2.sort()
        return freq1 == freq2
        
