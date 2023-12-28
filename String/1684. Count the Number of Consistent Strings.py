class Solution(object):
    def countConsistentStrings(self, allowed, words):
        # count = 0
        # for word in words:
        #     flag = True
        #     for i in word:
        #         if i not in allowed:
        #             flag = False
        #     if flag :
        #         count += 1

        # return count

        ans = len(words)
        for word in words:
            for a in word:
                if a not in allowed:
                    ans -=1
                    break
        return ans
        
            


        
