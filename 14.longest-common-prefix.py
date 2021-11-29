#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
         prefix = ''
         for char in zip(*strs):
            if len(set(char)) == 1:
                  prefix += char[0]
            else:
                  break
         return prefix
# @lc code=end

