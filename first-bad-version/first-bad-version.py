# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 0:
            return -1
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            ans = isBadVersion(mid)
            if ans == True:
                right = mid
            else:
                left = mid + 1
        return left