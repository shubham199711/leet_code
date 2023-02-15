class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowLen = len(grid)
        colLen = len(grid[0])
        rowCount0 = [x.count(0) for x in grid]
        rowCount1 = [rowLen - x for x in rowCount0]
        colCount0 = [x.count(0) for x in zip(*grid)]
        colCount1 = [colLen - x for x in colCount0]
        ans = []
        for row in range(rowLen):
            _ans = [rowCount1[row] + colCount1[col] - rowCount0[row] - colCount0[col] for col in range(colLen)]
            ans.append(_ans)
        return ans
        