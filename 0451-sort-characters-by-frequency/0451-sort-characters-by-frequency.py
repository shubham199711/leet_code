from queue import PriorityQueue
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        q = PriorityQueue()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for k,v in freq.items():
            q.put((-1 * v, k))
        ans = []
        while not q.empty():
            num, char = q.get()
            ans += [char] * (num * -1)
        return ''.join(ans)
        
            
        