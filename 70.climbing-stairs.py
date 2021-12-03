from typing import *
#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a, b = 1 , 2
        for _ in range(2, n):
            current = a + b
            a, b = b, current
        return b
# @lc code=end

