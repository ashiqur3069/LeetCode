class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine  =  magazine.replace(i,"",1)
        return True
            
