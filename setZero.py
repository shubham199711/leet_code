class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for r in range( len(matrix) ):
            for c in range( len(matrix[0]) ):
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)

        for r in rows:
            matrix[r] = [0]*len(matrix[0])

        for c in cols:
            for r in range( len(matrix) ):
                matrix[r][c] = 0

        return matrix