class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if not(i < len(obstacleGrid) and j < len(obstacleGrid[0])):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0 
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)
            
        return dfs(0, 0)
                
        