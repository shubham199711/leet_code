class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowCount0 = [x.count(0) for x in grid]
        rowCount1 = [x.count(1) for x in grid]
        colCount0 = [x.count(0) for x in zip(*grid)]
        colCount1 = [x.count(1) for x in zip(*grid)]
        ans = []
        for row in range(len(grid)):
            _ans = [rowCount1[row] + colCount1[col] - rowCount0[row] - colCount0[col] for col in range(len(grid[0]))]
            ans.append(_ans)
        return ans
        