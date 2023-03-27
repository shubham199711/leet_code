class Solution:
    def walk(self, grid , s, e, depth):
        if depth > self.count:
            return
        if not (0 <= s[0] < len(grid) and 0 <= s[1] < len(grid[0])):
            return
        if grid[s[0]][s[1]] == -1:
            return
        if grid[s[0]][s[1]] == 2:
            if depth == self.count:
                self.ans += 1
                return
        backUp = grid[s[0]][s[1]]
        grid[s[0]][s[1]] = -1 
        self.walk(grid, (s[0] + 1, s[1]), e, depth + 1)
        self.walk(grid, (s[0] - 1, s[1]), e, depth + 1)
        self.walk(grid, (s[0], s[1] + 1), e, depth + 1)
        self.walk(grid, (s[0], s[1] - 1), e, depth + 1)
        grid[s[0]][s[1]] = backUp
        
        
    
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
                    
        self.walk(grid, s, e, 1)
        return self.ans