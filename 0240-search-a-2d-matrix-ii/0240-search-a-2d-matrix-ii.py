class Solution:
    def searchMatrix(self, matrix, target):
        i, j = len(matrix)-1, 0
        while i>=0 and j<len(matrix[0]):
            if target == matrix[i][j]:
                return True
            if target<matrix[i][j]:
                i -= 1
            else:
                j += 1
        return False