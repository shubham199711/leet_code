from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if not(i < m and j < n):
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)
        return dfs(0 , 0)
