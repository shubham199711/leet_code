from typing import *
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) ->  Union[int, float]:
        _max = -float('inf')
        running_max = 0
        for item in nums:
            running_max = max(item , item + running_max)
            _max = max(_max,running_max)
        return _max
# @lc code=end

