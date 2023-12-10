class Solution(object):
    def reverseWords(self, s):
        """
        s = s + " "
        output = ""
        word = ''
        for i in s:
            if i != " ":
                word += i
            else:
                output += " " + word[::-1]  
                word = ''
        return output[1::] 
        
        """
      #Easy approch
        s =s.split(" ")
        array = []
        for i in s:
            array.append(i[::-1])
        return " ".join(array)
