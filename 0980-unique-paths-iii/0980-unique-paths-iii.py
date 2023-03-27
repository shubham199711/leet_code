class Solution:
    def walk(self, grid , s, e, visited):
        if s in visited:
            return
        if len(visited) > self.count:
            return
        if not (0 <= s[0] < len(grid) and 0 <= s[1] < len(grid[0])):
            return
        if grid[s[0]][s[1]] == -1:
            return
        if grid[s[0]][s[1]] == 2:
            if len(visited) == self.count - 1:
                self.ans += 1
                return
        visited.add(s)
        self.walk(grid, (s[0] + 1, s[1]), e, visited.copy())
        self.walk(grid, (s[0] - 1, s[1]), e, visited.copy())
        self.walk(grid, (s[0], s[1] + 1), e, visited.copy())
        self.walk(grid, (s[0], s[1] - 1), e, visited.copy())
        
        
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        s, e  = None, None
        self.count = 0
        self.ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count += 1
                    s = (i, j)
                if grid[i][j] == 2:
                    self.count += 1
                    e = (i, j)
                if grid[i][j] == 0:
                    self.count += 1
                    
        self.walk(grid, s, e, set([]))
        return self.ans