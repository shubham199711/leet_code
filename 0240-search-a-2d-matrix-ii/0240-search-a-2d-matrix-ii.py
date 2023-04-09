class Solution:
    def searchMatrix(self, matrix, target):
        result, i, j = False, len(matrix)-1, 0
        while i>=0 and j<len(matrix[0]):
            if target<matrix[i][j]:
                i -= 1
            elif target>matrix[i][j]:
                j += 1
            else:
                result = True
                break
        return result