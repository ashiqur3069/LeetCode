class RecentCounter(object):

    def __init__(self):
        self.list = []
        

    def ping(self, t):
        while self.list and t - self.list[0] > 3000:
            self.list.pop(0)
        self.list.append(t)
        return len(self.list)
        
