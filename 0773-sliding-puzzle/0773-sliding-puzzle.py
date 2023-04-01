class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ans = ((1,2,3),(4,5,0))
        index_i, index_j = 0, 0
        board_tuple = tuple(map(tuple, board))
        if board_tuple == ans:
            return 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    index_i, index_j = i, j
                    
        def bfs(i, j):
            stack = [(board, i, j, 1)]
            visited = set([board_tuple])
            while len(stack):
                _board, I, J , level = stack.pop(0)
                for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    _i = I + ii
                    _j = J + jj
                    __board  = copy.deepcopy(_board)
                    if not(0 <= _i < len(board) and 0 <= _j < len(board[0])): continue
                    __board[I][J], __board[_i][_j] = __board[_i][_j],  __board[I][J]
                    __board_tuple = tuple(map(tuple, __board))
                    if __board_tuple == ans:
                        return level
                    if __board_tuple not in visited:
                        stack.append((__board, _i, _j, level + 1))
                        visited.add(__board_tuple)
                        visited.add(__board_tuple)
            return -1
        return bfs(index_i, index_j)
        