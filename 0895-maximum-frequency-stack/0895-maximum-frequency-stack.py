class FreqStack(object):

    def __init__(self):
        self.d = defaultdict(int)
        self.array = []
        self.index = 0
        
    def push(self, val):
        self.d[val] += 1
        self.index += 1
        heapq.heappush(self.array, (-self.d[val], -self.index, val))
    
    def pop(self):
        count, index, val = heapq.heappop(self.array)
        self.d[val] -= 1
        return val
