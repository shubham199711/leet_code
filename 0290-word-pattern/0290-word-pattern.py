class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        cache = {}
        wordCache = {}
        for p, word in zip(pattern, s):
            if cache.get(p) is None:
                if wordCache.get(word) is None:
                    cache[p] = word
                    wordCache[word] = p
                elif wordCache[word] != p:
                    return False
            elif cache[p] != word:
                return False
        return True
        