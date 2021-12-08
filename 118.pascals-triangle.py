from typing import *
#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        _ans = []
        for i in range(numRows):
            if i > 1:
                _temp = [1]
                for _ in range(i - 1):
                    _temp.append(_ans[i - 1][len(_temp)] + _ans[i - 1][len(_temp) - 1])
                _temp.append(1)
                _ans.append(_temp)
            else:
                _ans.append([1 for _ in range(i + 1)])
        return _ans
        
# @lc code=end

