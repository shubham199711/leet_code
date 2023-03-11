class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bs():
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        i = bs()
        if i == 0:
            return arr[:k]
        elif i == len(arr):
            return arr[-k:]
        left, right = i - 1, i
        while k:
            leftElem = arr[left] if left >= 0 else float('-inf')
            rightElem = arr[right] if right < len(arr) else float('inf')
            if x - leftElem <= rightElem - x:
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left+1:right]
        
        