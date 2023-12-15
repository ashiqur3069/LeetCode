class Solution(object):
    def dayOfYear(self, date):
        dt = date.split('-')
        year = int(dt[0])
        month = int(dt[1])
        day = int(dt[2])
        L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year%400==0 or (year%100!=0 and year%4==0)):
            L[1] = L[1] + 1
        return day if month == 1 else sum(L[0:month]) - (L[month - 1] - day)
