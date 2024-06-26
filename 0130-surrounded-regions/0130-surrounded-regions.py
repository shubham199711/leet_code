class Solution:
    def solve(self, board):
        queue = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == 'O' and r in [0, len(board)-1] or c in [0, len(board[0])-1]) :
                    queue.append((r,c))
        while queue:
            r,c = queue.pop(0)
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'V'
                queue.append((r-1,c))
                queue.append((r+1,c))
                queue.append((r,c-1))
                queue.append((r,c+1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
