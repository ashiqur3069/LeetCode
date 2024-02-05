class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key = lambda x:x[1])
        arrow, last_val = 0, 0 
        for start, end in points:
            if arrow == 0 or start > last_val:
                arrow, last_val = arrow + 1, end
        return arrow

        
