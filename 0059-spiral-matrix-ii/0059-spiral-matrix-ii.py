class Solution:
    def generateMatrix(self, n):
        matrix = [[None]*n for _ in range(n)]
        rs,re,cs,ce = 0,n-1,0,n-1
        count = 1
        while rs <= re and cs <= ce:
            for j in range(cs, ce+1):
                matrix[rs][j], count = count, count+1
            for i in range(rs+1, re+1):
                matrix[i][ce], count = count, count+1
            for j in range(ce-1, cs-1, -1):
                matrix[re][j], count = count, count+1
            for i in range(re-1,rs,-1):
                matrix[i][cs], count = count, count+1
            rs, re = rs+1,re-1
            cs,ce = cs+1,ce-1
        return matrix