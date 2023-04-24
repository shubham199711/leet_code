class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word2 in word1:
            return len(word1) - len(word2)
        elif word1 in word2:
            return len(word2) - len(word1)
        
        m: int = len(word1)
        n: int = len(word2)
        
        @lru_cache(None)
        def helper(i: int, j: int):
            if i == m or j == n:
                return max(m - i, n - j)
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            return min(helper(i + 1, j), helper(i, j + 1)) + 1
        
        return helper(0, 0)