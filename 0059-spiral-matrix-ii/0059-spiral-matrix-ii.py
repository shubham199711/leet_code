class Solution2:
    def generateMatrix(self, n):
        matrix = [[None]*n for _ in range(n)]
        # r => row
        # c => col
        rs,re,cs,ce = 0,n-1,0,n-1
        count = 1
        while rs <= re and cs <= ce:
            for j in range(cs, ce+1): # fill from start till end
                matrix[rs][j], count = count, count+1
            for i in range(rs+1, re+1): # fill from start + 1 to end
                matrix[i][ce], count = count, count+1
            for j in range(ce-1, cs-1, -1): # fill from end -1 to end
                matrix[re][j], count = count, count+1
            for i in range(re-1,rs,-1): # full from end - 1 to start - 1(as 1 is already filled using start)
                matrix[i][cs], count = count, count+1
            rs, re = rs+1,re-1
            cs,ce = cs+1,ce-1
        return matrix

class Solution:
    def generateMatrix(self, n):
        ans = [[0]*n for _ in range(n)]
        x = y = j = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(1,n**2+1):
            ans[x][y] = i
            dx, dy = dirs[j]
            if 0<=x+dx<=n-1 and 0<=y+dy<=n-1 and ans[x+dx][y+dy]==0:
                x, y = x+dx, y+dy
            else:
                j = (j+1)%4
                dx, dy = dirs[j]
                x, y = x+dx, y+dy   
        return ans