from typing import *
#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        _bin = bin(n)[2:]
        _bin =  '0' * (32 - len(_bin)) + _bin
        return int(_bin[::-1], 2)
# @lc code=end

