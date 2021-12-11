from typing import *
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        _nums = collections.Counter(nums).most_common()
        for item,count in _nums:
            if count > majority:
                return item
        return -1
# @lc code=end

