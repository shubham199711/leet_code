from typing import *
#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d='0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        if columnNumber < 27:
            return d[columnNumber]
        while columnNumber > 0:
            columnNumber,r= divmod(columnNumber,26)
            if r == 0:
                columnNumber -= 1
                r += 26
            res = d[r] + res
        return res
# @lc code=end


