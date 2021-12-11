from typing import *
#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        # A
        # ord(s[i]) - 64 -> 1
        # (len(s) - i - 1)) -> (1 - 0 - 1) -> 0
        # 26 ** 0 -> 1
        # return 1
        return sum([(26 ** (len(s) - i - 1)) * (ord(s[i]) - 64) for i in range(len(s))])
# @lc code=end

