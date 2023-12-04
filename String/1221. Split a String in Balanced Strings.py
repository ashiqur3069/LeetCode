'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:
'''

class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        idx = 0
        for i in s:
            if i == "L":
                idx+=1
            else:
                idx-=1
            if idx == 0:
                count += 1
        return count
