from typing import *
#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        _ans = []
        for i in range(rowIndex + 1):
            if i > 1:
                _temp = [1]
                for _ in range(i - 1):
                    _temp.append(_ans[i - 1][len(_temp)] + _ans[i - 1][len(_temp) - 1])
                _temp.append(1)
                _ans.append(_temp)
            else:
                _ans.append([1 for _ in range(i + 1)])
        return _ans[-1]
        
# @lc code=end

