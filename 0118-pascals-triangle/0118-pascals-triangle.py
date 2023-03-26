class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            arr = [1] * (i + 1)
            for j in range(1, i):
                arr[j] = ans[-1][j - 1] + ans[-1][j]
            ans.append(arr)
        return ans
        