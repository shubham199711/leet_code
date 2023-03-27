class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(item):
            l, r = 0, len(item) - 1
            while l <= r:
                mid = (l + r) // 2
                if item[mid] == target:
                    return mid
                if item[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        def bsRow(item):
            l, r = 0, len(item) - 1
            while l <= r:
                mid = (l + r) // 2
                if item[mid][0] <= target <= item[mid][-1]:
                    return mid
                if item[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        index = bsRow(matrix)
        if index != -1:
            if bs(matrix[index]) >= 0:
                return True
        return False
        