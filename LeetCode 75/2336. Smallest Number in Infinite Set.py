'''
class SmallestInfiniteSet(object):

    def __init__(self):
        self.next_num = 1
        self.added_back_heap = []
        self.added_back_set = set()
        
    def popSmallest(self):
        if self.added_back_heap:
            smallest = heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
            return smallest
    
        num_to_return = self.next_num
        self.next_num += 1
        return num_to_return
        

    def addBack(self, num):
        if num < self.next_num and num not in self.added_back_set:
            self.added_back_set.add(num)
            heappush(self.added_back_heap, num)
'''
#Easy approch
class SmallestInfiniteSet(object):

    def __init__(self):
        self.present = [True for _ in range(1001)]    
    def popSmallest(self):
        for i in range(1,1001):
            if self.present[i] == True:
                self.present[i] = False
                return i

    def addBack(self, num):
        self.present[num] = True
