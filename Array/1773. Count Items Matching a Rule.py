class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        my_dict = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for i in items:
            if i[my_dict[ruleKey]] == ruleValue:
                count += 1
        return count
    '''
          cnt = 0

        if ruleKey == 'type':
            index = 0
        elif ruleKey == 'color':
            index = 1
        else:
            index = 2

        for item in items:
            if item[index] == ruleValue:
                cnt += 1

        return cnt
  '''
