#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, a):
        count = 0
        _len = len(a)
        i , l = 0, _len - 1
        while i < l:
            if a[i] == a[i+1]:
                count += 1
                del a[i+1]
                l -=1
            else :
                i +=1
        for _ in range(count + 1):
            a.append(-1) 
        return _len - count
# @lc code=end

