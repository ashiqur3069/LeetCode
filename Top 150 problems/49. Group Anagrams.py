class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[(ord(j) - ord("a"))]+= 1
            ans[tuple(count)].append(i)
        return ans.values()
        '''
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())
        '''
        
        
