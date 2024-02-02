class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # if newInterval comes before rest of the intervals
                result.append( newInterval )
                return result + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                # if newInterval does not merges with current interval and comes after it
                result.append(intervals[i])
            else:
                #overlaps and could overlap with next
                newInterval = [ min(newInterval[0] , intervals[i][0] ), max(newInterval[1] , intervals[i][1]) ]

        #if overlaps till last interval                
        result.append(newInterval)

        return result
