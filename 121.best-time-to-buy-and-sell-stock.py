from typing import *
#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_prof = 0
        _min = prices[0]
        for i in range(1 ,len(prices)):
            max_prof = max(max_prof, prices[i] - _min)
            _min = min(_min, prices[i])
        return max_prof
# @lc code=end

