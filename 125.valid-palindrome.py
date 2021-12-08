from typing import *
#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^A-Za-z0-9]", '', s).lower()
        return s == s[::-1]
        
# @lc code=end

