class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache  = {}
        for item in s:
            if cache.get(item) is not None:
                cache[item] += 1
            else:
                cache[item] = 1
        for i , item in enumerate(s):
            if cache[item] == 1:
                return i
        return -1
