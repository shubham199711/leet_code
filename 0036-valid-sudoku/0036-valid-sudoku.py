class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validArray(item):
            item = list(filter(lambda x: int(x) if x != '.' else False, item))
            if len(set(item)) != len(item):
                return False
            return True
            
        def vaildSubSet(sw,sc, ew, ec):
            cache = {}
            for i in range(sw, ew):
                for j in range(sc, ec):
                    if board[i][j] == '.':
                        continue
                    if cache.get(board[i][j]) is not None:
                        return False
                    cache[board[i][j]] = True
            return True
        for item in board:
            if not validArray(item):
                return False
        for item in zip(*board):
            if not validArray(item):
                return False
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not vaildSubSet(i,j, i + 3, j +3):
                    return False
        return True