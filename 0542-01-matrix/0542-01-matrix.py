class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        stack = []
        visited = set([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    stack.append((i, j))
                    visited.add((i, j))
        while len(stack):
            i, j = stack.pop(0)
            for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = i + ii
                jj = j + jj
                if not (0 <= ii < m and 0 <= jj < n): continue
                if (ii, jj) in visited: continue
                mat[ii][jj] += mat[i][j]
                visited.add((ii, jj))
                stack.append((ii, jj))
        return mat
        