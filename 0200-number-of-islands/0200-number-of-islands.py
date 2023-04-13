class Solution(object):
    def numIslands(self, grid):
        m , n = len(grid), len(grid[0])
        visited = set([])
        ans = 0
        def dfs(i,j):
            visited.add((i, j))
            for ii ,jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = i + ii
                jj = j + jj
                if (ii, jj) in visited:
                    continue
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == "1":
                    dfs(ii, jj)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    ans += 1
                    dfs(i,j)
        return ans
