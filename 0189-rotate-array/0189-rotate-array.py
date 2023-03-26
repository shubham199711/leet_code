class Solution:
    def swap(self, A, l, r):
        while l <= r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
        
    def rotate(self, A, k):
        N = len(A) - 1
        k %= (N + 1)
        self.swap(A, 0, N)
        self.swap(A, 0, k - 1)
        self.swap(A, k, N)
        
        
