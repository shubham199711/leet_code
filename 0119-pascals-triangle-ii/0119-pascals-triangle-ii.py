class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex + 1):
            _ans = [1]
            for j in range(1, i):
                _ans.append(ans[j -1] + ans[j])
            _ans.append(1)
            ans = _ans
        return ans
        
        