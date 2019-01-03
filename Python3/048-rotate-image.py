class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rcsize = len(matrix)
        for i in range(rcsize//2):
            for j in range(i, rcsize-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[rcsize-j-1][i]
                matrix[rcsize-j-1][i] = matrix[rcsize-i-1][rcsize-j-1]
                matrix[rcsize-i-1][rcsize-j-1] = matrix[j][rcsize-i-1]
                matrix[j][rcsize-i-1] = temp
        pass
