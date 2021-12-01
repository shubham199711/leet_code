#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val):
        count = 0 
        i , l = 0 , len(nums)
        while i < l:
            if nums[i] == val:
                count += 1
                del nums[i]
                l -= 1
            else:
                i += 1
        for _ in range(count):
            nums.append(-1)
        return len(nums) - count
# @lc code=end

