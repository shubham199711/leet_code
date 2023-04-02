class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        stack = []
        visited = set([])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append((i, j, 1))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    count += 1
                    
        if count == 0:
            return 0
        
        while len(stack):
            i, j, level = stack.pop(0)
            for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = i + ii
                jj = j + jj
                if not(0 <= ii < m and 0 <= jj < n): continue
                if (ii, jj) in visited: continue
                if grid[ii][jj] != 1: continue
                grid[ii][jj] = 2
                count -= 1
                if count == 0:
                    return level
                visited.add((ii, jj))
                stack.append((ii, jj, level + 1))
            
        return -1
                    
        