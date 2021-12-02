from typing import *
#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List, target):
        for index, item in enumerate(nums):
            if item == target:
                return index
            if item > target:
                return index
        return len(nums)
# @lc code=end

