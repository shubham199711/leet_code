class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = []
        m , n = len(board), len(board[0])
        seen = [[False] * n for x in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    stack.append((i, j))
                                 
        def dfs(i, j, index):
            # print(i, j, index, seen)
            if index == len(word):
                return True
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii, jj = i + ii, j + jj
                if not (0<= ii < m and 0<= jj < n): continue
                if seen[ii][jj]: continue
                if word[index] == board[ii][jj]:
                    seen[ii][jj] = True
                    if dfs(ii, jj, index + 1):
                        return True
                    seen[ii][jj] = False
            return False
                    
        for (i, j) in stack:
            seen[i][j] = True
            if dfs(i, j, 1):
                return True
            seen[i][j] = False
        return False
        