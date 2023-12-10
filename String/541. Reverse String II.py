'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
'''
class Solution(object):
    def reverseStr(self, s, k):
        ans = ''
        for i in range(len(s)//k+1):
            ans += s[i*k:(i+1)*k][::(-1)**(i+1)]
        return ans
