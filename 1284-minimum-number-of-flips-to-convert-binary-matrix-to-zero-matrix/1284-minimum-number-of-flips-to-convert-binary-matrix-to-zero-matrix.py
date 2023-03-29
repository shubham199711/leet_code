class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def checkAllZero(_mat):
            for i in range(len(_mat)):
                for j in range(len(_mat[0])):
                    if _mat[i][j] != 0:
                        return False
            return True
        
        def flip(__mat, i, j):
            _mat = copy.deepcopy(__mat)
            _mat[i][j] = int(not _mat[i][j])
            if i + 1 < len(_mat): # down
                _mat[i + 1][j] = int(not _mat[i + 1][j])
            if i - 1 >= 0: # up
                _mat[i - 1][j] = int(not _mat[i - 1][j])
            if j + 1 < len(_mat[0]): # right
                _mat[i][j + 1] = int(not _mat[i][j + 1])
            if j - 1 >= 0: # left
                _mat[i][j - 1] = int(not _mat[i][j - 1])
            return _mat
        
        visited = set()
        queue = collections.deque([[mat, 0]])
        while queue:
            for _ in range(len(queue)):
                cmat, cnt = queue.popleft()
                if checkAllZero(cmat): return cnt
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        nmat = flip(cmat, i, j)
                        cur = tuple(map(tuple, nmat))
                        if cur in visited: continue
                        queue.append([nmat, cnt+1])
                        visited.add(cur)
        return -1
        return -1
       