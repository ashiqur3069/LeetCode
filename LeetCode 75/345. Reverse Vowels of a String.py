class Solution(object):
    def reverseVowels(self, s):
        array = list(s)
        vowel = "aeiouAEIOU"
        i,j = 0,len(s)-1

        while i<j:
            if array[i] in vowel and array[j] in vowel:
                array[i],array[j] = array[j],array[i]
                i += 1
                j -= 1
            if array[i] not in vowel:
                i+=1
            if array[j] not in vowel:
                j-=1
        return "".join(array)
