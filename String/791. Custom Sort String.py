class Solution(object):
    def customSortString(self, order, s):
        my_dict = {}
        new_s = set(s)
        for i in new_s:
            my_dict[i] = s.count(i)
        string = ""
        for i in order:
            if i in my_dict.keys():
                string += my_dict[i]*i
                my_dict.pop(i)
        for i, j in my_dict.items():
            string += i * j
        return string


        
        
