#question

'''There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.'''

         '''
         Approch:
         First, reverse sort the array. Then, start loop from 2nd value which is my first coin. 
         Bob's coins lies in the last side of the array, which is equal to total piles in array, i.e. len/3.
         End loop before Bob's value. Increment by two.
                                                          '''


class Solution(object):
    def maxCoins(self, piles):
        piles = sorted(piles, reverse = True)
        my_max_coin = 0
        for i in range(1,len(piles)-(len(piles)/3),2):
         
            my_max_coin += piles[i]
        return my_max_coin
piles = [9,8,7,6,5,1,2,3,4]
solution = Solution()
Result = solution.maxCoins(piles)
print(Result)
