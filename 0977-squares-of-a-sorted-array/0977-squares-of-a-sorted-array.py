class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        A = [x * x for x in A]
        l,r = 0, len(A) - 1
        for i in range(len(A)):
            if A[l] >= A[r]:
                res[~i] = A[l]
                l += 1
            else:
                res[~i] = A[r]
                r -= 1
        return res
                
