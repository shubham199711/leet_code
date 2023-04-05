class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def bfs(i, j):
            if i == len(triangle):
                return 0
            return triangle[i][j] + min(bfs(i + 1, j), bfs(i + 1, j + 1))
        return bfs(0,0)
            
        