class Solution(object):
    def largestAltitude(self, gain):
        array = [0]
        for i in gain:
            array.append(array[-1] + i)
        return max(array)
