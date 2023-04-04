class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for x in range(n)]
        ans = []
        def validPlacement(r, c):
            for i in range(n):
                if i == r: continue
                if board[i][c] == 'Q':
                    return False
            for i, j in [(1, 1),(1, -1),(-1, -1),(-1, 1)]:
                _r,  _c = r + i, c + j
                while 0 <= _r < n and 0 <= _c < n:
                    if board[_r][_c] == 'Q':
                        return False
                    _r,  _c = _r + i, _c + j
            return True
            
        def backtrack(row):
            if row == n:
                ans.append(list(map(lambda x: ''.join(x), board)))
                return
            for i in range(n):
                board[row][i] = 'Q'
                if validPlacement(row, i):
                    backtrack(row + 1)
                board[row][i] = '.'
        backtrack(0)
        return ans
        