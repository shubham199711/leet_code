from typing import *
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for item in nums:
            if nums.count(item) == 1:
                return item
        return -1
# @lc code=end

