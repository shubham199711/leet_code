class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowLen = len(grid)
        colLen = len(grid[0])
        rowCount0, rowCount1 = [], []
        colCount0, colCount1 = [], []
        for x in grid:
            count = x.count(0)
            rowCount0.append(count)
            rowCount1.append(rowLen - count)
        for x in zip(*grid):
            count = x.count(0)
            colCount0.append(count)
            colCount1.append(colLen - count)
        ans = []
        for row in range(rowLen):
            _ans = [rowCount1[row] + colCount1[col] - rowCount0[row] - colCount0[col] for col in range(colLen)]
            ans.append(_ans)
        return ans
        