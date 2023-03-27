class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            if item[0] <= target <= item[-1]:
                l, r = 0, len(item) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if item[mid] == target:
                        return True
                    if item[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
        return False
        