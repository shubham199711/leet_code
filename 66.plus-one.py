from typing import *
#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            _str = [str(x) for x in digits]
            _str = ''.join(_str)
            _str = str(int(_str) + 1)
            return [int(x) for x in _str]
        digits[-1] += 1
        return digits
# @lc code=end

