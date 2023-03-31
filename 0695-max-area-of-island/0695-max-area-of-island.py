class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set([])
        def dfs(i , j, level):
            visited.add((i, j))
            for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                _i = i + ii
                _j = j + jj
                if not(0 <= _i < len(grid) and 0 <= _j < len(grid[0])) : continue
                item = grid[_i][_j]
                if item == 1 and (_i, _j) not in visited:
                    level += (dfs(_i, _j, 1))
            return level
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                item = grid[i][j]
                if item == 1 and (i, j) not in visited:
                    ans = max(ans, dfs(i, j, 1))
        return ans       
                    
        