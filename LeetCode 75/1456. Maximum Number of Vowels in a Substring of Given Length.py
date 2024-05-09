class Solution(object):
    def maxVowels(self, s, k):
        vowel = "aeiou"
        current_v = 0
        for i in range(k):
            if s[i] in vowel:
                current_v += 1
        result = current_v

        for i in range(k,len(s)):
            if s[i] in vowel:
                current_v += 1
            if s[i-k] in vowel:
                current_v -= 1
            result = max(current_v,result)
        return result
