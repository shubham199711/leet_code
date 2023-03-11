class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num + 1
        while left <= right:
            mid = (left + right) // 2
            squere = mid * mid
            if squere == num:
                return True
            if squere < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
        