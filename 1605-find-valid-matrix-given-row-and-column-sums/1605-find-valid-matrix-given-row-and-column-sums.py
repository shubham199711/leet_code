class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row, col = len(rowSum), len(colSum)
        ans = [ [0]*col for _ in range(row) ]
        for i in range(row):
            for j in range(col):
                val = min(rowSum[i], colSum[j])
                rowSum[i] -= val
                colSum[j] -= val
                ans[i][j] = val
        return ans