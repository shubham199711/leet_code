from typing import *
#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for index in range(m, len(nums1)):
            nums1[index] = nums2[m - index]
        nums1.sort()
        
# @lc code=end

