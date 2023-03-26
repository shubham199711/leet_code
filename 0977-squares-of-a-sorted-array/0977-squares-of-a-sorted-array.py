class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        l,r = 0, len(A) - 1
        for i in range(len(A)):
            if abs(A[l]) >= abs(A[r]):
                res[~i] = A[l] * A[l]
                l += 1
            else:
                res[~i] = A[r] * A[r]
                r -= 1
        return res
                
