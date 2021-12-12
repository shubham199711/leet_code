from typing import *
#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapping2 = {}
        for index,item in enumerate(s):
            if mapping.get(t[index]) is not None:
                if str(mapping[t[index]]) != str(item):
                    return False
            if mapping2.get(item) is not None:
                if str(mapping2[item]) != str(t[index]):
                    return False
            mapping[t[index]] = item
            mapping2[item] = t[index]
        return True
# @lc code=end

