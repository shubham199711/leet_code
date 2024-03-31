from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums, k):
        q = PriorityQueue()
        cache = {}
        for item in nums:
            cache[item] = cache.get(item, 0) + 1
        for key, value in cache.items():
            q.put((-1 * value, key))
        return [q.get()[1] for _ in range(k)]
                
                
                
            
            