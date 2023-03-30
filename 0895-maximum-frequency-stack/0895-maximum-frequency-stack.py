class FreqStack(object):

    def __init__(self):
        self.d = defaultdict(int)
        self.stack = []
        self.i = 0
        
    def push(self, val):
        self.d[val]+=1
        self.i+=1
        heapq.heappush(self.stack, (-self.d[val], -self.i, val))
    
    def pop(self):
        cnt, location, val = heapq.heappop(self.stack)
        self.d[val]-=1
        return val