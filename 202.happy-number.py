from typing import *
#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
memo = {}
class Solution:
    def square(self, n:int) -> int:
        if memo.get(n) is not None:
            return memo[n]
        memo[n] = n * n
        return memo[n]
        
    def isHappy(self, n: int) -> bool:
        isSeen = {}
        while True:
            _n = map(int,str(n))
            _sum = 0
            for item in _n:
                _sum += self.square(item)
            n = _sum
            if isSeen.get(n):
                return False
            if n == 1:
                return True
            isSeen[n] = True
        return False
# @lc code=end

