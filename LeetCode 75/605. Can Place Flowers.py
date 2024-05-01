class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        new_array = [0] + flowerbed + [0]

        for i in range(1,len(new_array)-1):
            if new_array[i-1] == 0 and new_array[i] == 0 and new_array[i+1] == 0:
                new_array[i] = 1
                n -=1
        return True if n <= 0 else False
