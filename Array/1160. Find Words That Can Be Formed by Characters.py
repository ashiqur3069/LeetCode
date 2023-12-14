'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

'''

class Solution(object):
    def countCharacters(self, words, chars):
        ans = 0
        for i in words:
            ch =chars
            l = 0
            for j in i:
                if j in ch:
                    ch=ch.replace(j,"",1)
                    l+=1
            if l == len(i):
                ans+=len(i)
        return ans
###################################################################################
      #Easy way:
        sum = 0
        for word in words:
            for char in word:
                if word.count(char) > chars.count(char):
                    break
            else:
                sum += len(word)
                
        return sum

        
