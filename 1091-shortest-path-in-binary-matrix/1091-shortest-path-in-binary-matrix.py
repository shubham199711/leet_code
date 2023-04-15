from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] == 1
        while queue:
            i , j, level = queue.popleft()
            if i == (n - 1) and j == (n - 1):
                return level
            for ii, jj in [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]:
                ii = i + ii
                jj = j + jj
                if not(0 <= ii < n and 0 <= jj < n) or grid[ii][jj] == 1:
                    continue
                grid[ii][jj] = 1
                queue.append((ii, jj, level + 1))
        return -1
