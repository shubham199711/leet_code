class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(x,y):
            if x==m-1 and y==n-1:
                return max(1,-grid[x][y]+1)
            if x>=m or y>=n:
                return float('inf')
            return max(1,min(dp(x+1,y),dp(x,y+1))-grid[x][y])
        
        m,n=len(grid),len(grid[0])
        return dp(0,0)