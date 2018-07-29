class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowsize = len(matrix)
        colsize = len(matrix[0])
        row0 = 1
        col0 = 1
        for i in range(rowsize):
            for j in range(colsize):
                if matrix[i][j] == 0:
                    if i==0:
                        row0 = 0
                    if j==0:
                        col0 = 0
                    matrix[i][0] = matrix[0][j] = 0
        for j in range(1, colsize):
            if matrix[0][j] == 0:
                for y in range(rowsize):
                    matrix[y][j] = 0
        for i in range(1, rowsize):
            if matrix[i][0] == 0:
                for x in range(colsize):
                    matrix[i][x] = 0
        if col0 == 0:
            for y in range(rowsize):
                matrix[y][0] = 0
        if row0 == 0:
            for x in range(colsize):
                matrix[0][x] = 0
        pass
