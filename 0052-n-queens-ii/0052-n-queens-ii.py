class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        
        def add_to_visited(visited, i, j):
            _visited = copy.deepcopy(visited)
            
            for jj in range(n):
                _visited.add((i, jj))
                
            for jj in range(n):
                _visited.add((jj, j))
                
            # up 
            ii, jj = i , j
            while ii >= 0 and jj > 0:
                _visited.add((ii, jj))
                ii -= 1
                jj -= 1
                
            ii, jj = i , j
            while ii >= 0 and jj >= 0:
                _visited.add((ii, jj))
                ii -= 1
                jj += 1
                
            # down 
            ii, jj = i , j
            while ii < n and jj >= 0:
                _visited.add((ii, jj))
                ii += 1
                jj -= 1
                
            ii, jj = i , j
            while ii < n and jj < n:
                _visited.add((ii, jj))
                ii += 1
                jj += 1
            return _visited
        
        def dfs(i, visited):
            nonlocal ans
            if i == n:
                ans += 1
                return
            for jj in range(n):
                if (i, jj) not in visited:
                    _visited = add_to_visited(visited, i, jj)
                    dfs(i + 1, _visited)
        
        dfs(0, set([]))
        return ans
            
            
        