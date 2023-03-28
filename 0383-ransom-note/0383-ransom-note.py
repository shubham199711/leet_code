class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cache = {}
        for item in magazine:
            if cache.get(item) is not None:
                cache[item] += 1
            else:
                cache[item] = 1
        for item in ransomNote:
            if cache.get(item) is not None and cache[item] > 0:
                cache[item] -= 1
            else:
                return False
        return True 
        