def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # assuming square matrix i.e. len(matrix[0]) = len(matrix)
    rcsize = len(matrix)
    for i in range(rcsize/2):
        for j in range(i, rcsize-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[rcsize-j-1][i]
            matrix[rcsize-j-1][i] = matrix[rcsize-i-1][rcsize-j-1]
            matrix[rcsize-i-1][rcsize-j-1] = matrix[j][rcsize-i-1]
            matrix[j][rcsize-i-1] = temp
    pass

# matrix =[
#   [ 1, 2, 3, 4, 5],
#   [ 6, 7, 8, 9, 10],
#   [11, 12, 13, 14, 15],
#   [16,17,18,19, 20],
#   [21,22,23,24,25]
# ]
# rotate(matrix)
# for i in matrix:
#     print i, " "

# matrix =[
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
# rotate(matrix)
# print(matrix)

# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# rotate(matrix)
# print(matrix)
