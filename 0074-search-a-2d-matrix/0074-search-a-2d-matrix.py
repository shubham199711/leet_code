class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        def bs_array():
            left, right = 0, len(m) - 1
            while left <= right:
                mid = (left + right) // 2
                if m[mid][0] <= target <= m[mid][-1]:
                    return mid
                elif m[mid][-1] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def bs(_list):
            left, right = 0, len(_list) - 1
            while left <= right:
                mid = (left + right) // 2
                if _list[mid] == target:
                    return True
                elif _list[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        
        index = bs_array()
        if index == -1:
            return False
        return bs(m[index])
        
