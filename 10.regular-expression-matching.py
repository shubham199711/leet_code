#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
import  re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match(f'^{p}$',s)
# @lc code=end

