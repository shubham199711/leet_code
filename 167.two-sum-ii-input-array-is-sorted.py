from typing import *
#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff_dict = {}
        for index, item in enumerate(numbers):
            if diff_dict.get(item) is not None:
                return [diff_dict.get(item) + 1, index + 1]
            diff = target - item
            diff_dict[diff] = index
        return []
# @lc code=end

