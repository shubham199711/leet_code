class MyHashMap:

    def __init__(self):
        self.n = 1000
        self.table = []
        for i in range(self.n):
            self.table.append([])
    def find(self,key):
        hk = key % self.n
        for i,v in enumerate(self.table[hk]):
            if v[0]==key:
                return hk,i
        return hk,-1
    
    def put(self, key: int, value: int) -> None:
        hk,idx = self.find(key)
        if idx!=-1:
            # replace value
            self.table[hk][idx] = (key,value)
        else:
            # add new value
            self.table[hk].append((key,value))

    def get(self, key: int) -> int:
        hk,idx = self.find(key)
        if idx!=-1:
            return self.table[hk][idx][1]
        else:
            return -1
                
                
    def remove(self, key: int) -> None:
        hk,idx = self.find(key)
        if idx!=-1:
            del self.table[hk][idx]

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)